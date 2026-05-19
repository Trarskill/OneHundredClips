# OneHundredClips: Analysis 100 TikTok 

<div align="center">
  <a href="README.md">🇬🇧 English </a> | 
  <a href="README.ua.md">🇺🇦 Українська</a> | 
  <a href="README.es.md">🇪🇸 Español</a>
</div>

---

### 🖥️ Plataforma:
**PC - Windows**

--- 

### 📘 Descripción:
Este es un programa sencillo para contar y analizar videos vistos (por ejemplo, en TikTok, Reels, Shorts). 
El objetivo general es ver 100 o más videos y categorizarlos:
  - 🟢 Bueno / Útil
  - 🟡 Neutral
  - 🔴 Malo / Degradante

Esta aplicación ayuda a que el análisis del consumo de contenido sea más simple y visual.

---

### 📸 Capturas de pantalla:
* **Selector de idioma al inicio:**
  <br>![Language Selector](assets/screenshot-at-launch-language-selector.png)
* **Ventana principal:**
  <br>![Main Window](assets/screenshot-main-window.png)
* **Menú:**
  <br>![Popup Menu](assets/screenshot-popup-menu-window.png)
* **Editor de criterios:**
  <br>![Criteria Editor](assets/screenshot-criteria-editor.png)
* **Guardar en archivo:**
  <br>![Saved to File](assets/screenshot-saved-to-file.png)
* **Visor de historial:**
  <br>![History Viewer](assets/screenshot-history-viewer.png)

---

### 🛠️ Tecnologías: 
- **Python 3.12**
- **Tkinter ( Interfaz Gráfica / GUI )**
- **JSON ( Persistencia de Datos y Configuración )**

--- 

### 🚀 Cómo ejecutar:

Asegúrate de tener instalado Python 3.12+.

```bash
  cd OneHundredClips
  python main.py
```

---

### 🏗️ Arquitectura del proyecto:

Siguiendo el principio de separación de responsabilidades, la estructura del proyecto está estrictamente dividida en código fuente, datos del usuario y archivos de localización:

```bash
OneHundredClips/

├── locales/                  # 🌐 Archivos de idioma i18n
├── user_data/                # 📂 Datos generados por el usuario
│   ├── save/                 # Historial de informes diarios
│   ├── settings.json         # Configuración del usuario y criterios personalizados
│   └── data.json             # Sesión de conteo actual
├── src/                      # 💻 Código fuente
│   ├── config.py             # Configuraciones globales e i18n
│   ├── storage.py            # Lógica de persistencia de datos
│   ├── app_logic.py          # Lógica y matemáticas centrales de la aplicación
│   └── gui/                  # 🎨 Interfaz gráfica de usuario
│       ├── main_window.py    # Configuración de la interfaz principal y cuadrícula
│       ├── windows/          # Ventanas emergentes separadas
│       └── components/       # Componentes de interfaz reutilizables
├── assets/                   # 📸 Capturas de pantalla para README
├── README.es.md              # Documentación del proyecto
└── main.py                   # 🚀 Punto de entrada de la aplicación
```
---

### 📈 Futuras mejoras:
1. [+] Añadir la posibilidad de seleccionar de una lista al presionar un botón, y la opción de desactivar esta función.
2. [+] Informe más detallado con los resultados de las pulsaciones de botones y opciones seleccionadas.
3. [+] Creación de una selección personalizada desde la lista para el botón dentro de la aplicación + guardar en un archivo JSON.
4. [+] Edición del texto de los criterios (añadir criterios propios) en la propia aplicación + guardar en un archivo JSON.
5. [+] Cargar y ver archivos de guardado anteriores directamente en la aplicación.
6. [+] Añadir diferentes idiomas de interfaz (i18n).
7. [?] Otros...

---
*(MY APP #2)*