from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from textblob import TextBlob
import time
import matplotlib.pyplot as plt
import pandas as pd
import os
import re


# EXTRACCIÓN DE COMENTARIOS DE FACEBOOK
# --------------------------------------------------------------------------------------------
# Configuración del driver de Selenium
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Función para iniciar sesión en Facebook
def login_facebook(driver, email, password):
    driver.get("https://www.facebook.com")
    time.sleep(2)
    
    # Localizar el campo de email y enviar el email
    email_elem = driver.find_element(By.ID, "email")
    email_elem.send_keys(email)
    
    # Localizar el campo de contraseña y enviar la contraseña
    password_elem = driver.find_element(By.ID, "pass")
    password_elem.send_keys(password)
    
    # Enviar la contraseña y presionar Enter para iniciar sesión
    password_elem.send_keys(Keys.RETURN)
    time.sleep(5)  # Espera para asegurarse de que la sesión se ha iniciado

# Función para obtener las URLs de las publicaciones recientes de una página
def scrape_facebook_page(driver, page_url):
    driver.get(page_url)
    time.sleep(5)  # Espera para que la página cargue completamente
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Espera para que carguen más publicaciones

    # Filtrar publicaciones solo de la página específica
    posts = driver.find_elements(By.XPATH, "//div[@role='article']//a[contains(@href, '/posts/')]")
    post_urls = [post.get_attribute('href') for post in posts if post.get_attribute('href') and 'facebook.com/gustavopetrourrego/posts' in post.get_attribute('href')]
    return post_urls

# Función para extraer comentarios de una publicación específica
def scrape_comments_from_post(driver, post_url):
    driver.get(post_url)
    time.sleep(5)  # Espera para que la página de la publicación cargue completamente

    # Expandir todos los comentarios si es necesario
    for _ in range(5):  # Intentar hacer clic en "Ver más comentarios" hasta 5 veces
        try:
            more_comments_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Ver más comentarios')]")
            more_comments_button.click()
            time.sleep(2)  # Espera breve para que carguen los nuevos comentarios
        except Exception as e:
            break  # Salir del bucle si no se encuentra el botón

    # Capturar todos los comentarios visibles
    comments = driver.find_elements(By.XPATH, "//div[@class='x1lliihq xjkvuk6 x1iorvi4']//div[@dir='auto']")
    comment_texts = [comment.text for comment in comments if comment.text]
    print(f"Se encontraron {len(comment_texts)} comentarios en la publicación: {post_url}")
    return comment_texts

# Credenciales de Facebook
email = "correo"
password = "contraseña"

# Iniciar sesión en Facebook
login_facebook(driver, email, password)

# Páginas de Facebook a scrape
pages = ['https://www.facebook.com/gustavopetrourrego']
all_comments = []
for page in pages:
    print(f"Scrapeando página: {page}")
    post_urls = scrape_facebook_page(driver, page)[:5]  # Limitar a las últimas 5 publicaciones
    for post_url in post_urls:
        print(f"Scrapeando comentarios de la publicación: {post_url}")
        comments = scrape_comments_from_post(driver, post_url)
        all_comments.extend(comments)
driver.quit()

# Guardar los datos en un archivo CSV
if all_comments:
    df = pd.DataFrame(all_comments, columns=["Comentario"])
    output_path = os.path.join(os.getcwd(), 'Comentarios_Facebook.csv')
    df.to_csv(output_path, index=False)
    print(f"Datos guardados en {output_path}")
else:
    print("No se encontraron comentarios.")


# TRANSFORMACION DE DATOS Y ANALISIS DE SENTIMIENTOS
# --------------------------------------------------------------------------------------------
# Función para limpiar y normalizar los comentarios
def clean_comment(comment):
    # Convertir a minúsculas
    comment = comment.lower()
    # Eliminar URLs
    comment = re.sub(r'http\S+', '', comment)
    # Eliminar caracteres especiales y números
    comment = re.sub(r'[^a-zA-Z\s]', '', comment)
    # Eliminar espacios adicionales
    comment = re.sub(r'\s+', ' ', comment).strip()
    return comment

# Función para analizar el sentimiento de un comentario usando TextBlob
def analyze_sentiment(comment):
    analysis = TextBlob(comment)
    # Determinar sentimiento: positivo, negativo o neutral
    if analysis.sentiment.polarity > 0:
        return 'positivo'
    elif analysis.sentiment.polarity < 0:
        return 'negativo'
    else:
        return 'neutral'

# Cargar los comentarios extraídos
input_path = 'Comentarios_Facebook.csv'
df = pd.read_csv(input_path)

# Limpiar y analizar el sentimiento de cada comentario
df['Comentario_Limpio'] = df['Comentario'].apply(clean_comment)
df['Sentimiento'] = df['Comentario_Limpio'].apply(analyze_sentiment)

# Guardar los resultados en un nuevo archivo CSV
output_path = 'Comentarios_Facebook_Analizados.csv'
df.to_csv(output_path, index=False)
print(f"Análisis de sentimientos guardado en {output_path}")


# ANÁLISIS Y VISUALIZACIÓN DE DATOS
# --------------------------------------------------------------------------------------------
# Análisis básico de sentimientos
sentiment_counts = df['Sentimiento'].value_counts()

# Visualización de la distribución de sentimientos
plt.figure(figsize=(8,6))
sentiment_counts.plot(kind='bar', color=['gray', 'green', 'red'])
plt.title('Distribución de Sentimientos en Comentarios de Facebook')
plt.xlabel('Sentimiento')
plt.ylabel('Cantidad de Comentarios')
plt.xticks(rotation=0)
plt.show()