# Manual de Despliegue en la Nube Gratuito (Sin Límites)
### GitHub Pages + Firebase Realtime Database (Móvil y Escritorio)

Este manual te explica paso a paso cómo subir tu aplicación a **GitHub Pages** de forma gratuita e ilimitada (sin renovaciones de 30 días) y conectarla con una base de datos en la nube de **Firebase** para que el residente y los administradores puedan guardar y sincronizar comentarios desde cualquier celular (Android o iPhone/Safari) desde internet.

---

## 💻 Paso 1: Configurar la Base de Datos en Firebase (100% Gratis)

Para que los comentarios y estados se guarden de forma compartida en internet, usaremos **Firebase Realtime Database** (el plan gratuito de Google que nunca vence y soporta hasta 100 usuarios simultáneos).

1. Ingresa a la consola de Firebase: [console.firebase.google.com](https://console.firebase.google.com/) con tu cuenta de Gmail.
2. Haz clic en **Crear un proyecto** (ej. `seguimiento-cabanillas`). Desactiva Google Analytics si lo prefieres para agilizar el proceso y crea el proyecto.
3. En el menú lateral izquierdo, haz clic en **Compilación (Build)** y selecciona **Realtime Database**.
4. Haz clic en **Crear base de datos**, selecciona la ubicación del servidor (puedes elegir cualquiera, ej. Estados Unidos) y haz clic en Siguiente.
5. Selecciona la opción **Comenzar en modo de prueba** (esto activa los permisos de lectura y escritura iniciales) y haz clic en **Habilitar**.
6. **Copia la URL** que te proporciona Firebase (se encuentra en la parte superior del panel, ej: `https://seguimiento-cabanillas-default-rtdb.firebaseio.com/`).
7. En la pestaña **Reglas (Rules)** del panel de la base de datos, asegúrate de que figuren así para que la web pueda conectarse sin autenticación compleja:
   ```json
   {
     "rules": {
       ".read": "true",
       ".write": "true"
     }
   }
   ```
   *(Si realizas cambios en el JSON de las Reglas, haz clic en el botón azul **Publicar**).*

---

## 🛠️ Paso 2: Vincular la Base de Datos en el HTML

Ahora enlazaremos la aplicación con tu base de datos de Firebase:

1. Abre el archivo [index.html](file:///d:/11%20APPS/04%20SEG.%20DE%20REQ/index.html) (o `SEGUIMIENTO_REQUERIMIENTOS.html`) en tu editor.
2. Busca la línea de configuración `const DATABASE_URL` (se encuentra en el inicio de la sección `<script>`, aproximadamente en la línea 2480):
   ```javascript
   const DATABASE_URL = "/api/requirements";
   ```
3. Reemplaza `"/api/requirements"` por la **URL de tu base de datos de Firebase**, asegurándote de colocar **`requirements.json`** al final. Por ejemplo:
   ```javascript
   const DATABASE_URL = "https://seguimiento-cabanillas-default-rtdb.firebaseio.com/requirements.json";
   ```
4. Guarda el archivo.
5. Abre la aplicación en tu navegador de forma local. Al guardar cualquier cambio, se subirá automáticamente a tu base de datos en la nube.

---

## 🚀 Paso 3: Publicar la App en GitHub Pages (Gratis e Ilimitado)

Para subir los archivos a GitHub y habilitar el enlace público para los celulares:

1. Crea una cuenta gratuita en [github.com](https://github.com/) si aún no tienes una.
2. Descarga e instala **GitHub Desktop** ([desktop.github.com](https://desktop.github.com/)) en tu computadora.
3. En GitHub Desktop:
   * Ve a **File > New Repository**.
   * Ponle de nombre al repositorio exactamente el nombre de tu carpeta en GitHub (en tu caso: `Seguimiento-de-obra`).
   * Selecciona la carpeta local de tu proyecto (`d:\11 APPS\04 SEG. DE REQ`) como la ruta local.
   * Haz clic en **Create Repository**.
4. Haz clic en el botón **Publish Repository** para subirlo a tu cuenta de GitHub.
5. Ingresa a la web de GitHub en tu navegador, ve a tu repositorio (`github.com/tecnocaba/Seguimiento-de-obra`):
   * Haz clic en la pestaña **Settings** (Configuración) arriba a la derecha.
   * En el menú lateral izquierdo, selecciona **Pages**.
   * En la sección "Build and deployment", cambia la rama (Branch) de `None` a **`main`** (o `master`) y la carpeta a `/ (root)`. Haz clic en **Save**.
6. **Resolución del Error 404**: GitHub Pages requiere de forma obligatoria un archivo llamado `index.html` en la raíz del proyecto para servir la dirección principal. He duplicado tu archivo principal como `index.html`. 
   Ahora, al ingresar a tu dirección principal:
   `https://tecnocaba.github.io/Seguimiento-de-obra/`
   La aplicación cargará de manera automática e instantánea sin dar error de archivo no encontrado (404).

---

## 📱 Paso 4: Instalar en Celulares (Android / Safari)

Una vez publicada la web en GitHub Pages:

* **En Android (Chrome / Edge)**:
  1. Abre el enlace en Chrome.
  2. Presiona el botón amarillo **"Instalar App"** con la animación de latido en el encabezado.
  3. Confirma la instalación.
* **En iPhone / iOS (Safari)**:
  1. Abre el enlace en Safari.
  2. Presiona el botón **Compartir** (cuadrado con flecha hacia arriba) en la parte inferior.
  3. Desplázate hacia abajo y presiona **"Añadir a la pantalla de inicio"** (Add to Home Screen).

*La App se añadirá a la pantalla de inicio como una aplicación nativa. Al abrirla, se conectará a la base de datos de Firebase y sincronizará todos los requerimientos y bitácoras de comentarios en tiempo real.*

---

## 🖨️ Paso 5: Impresión de Reportes A4 Horizontal

1. Abre el detalle de cualquier requerimiento presionando **"Ver"**.
2. Haz clic en **"🖨 Imprimir A4"** en la parte inferior izquierda.
3. En la ventana de tu navegador o celular:
   * Selecciona la orientación **Horizontal (Landscape)**.
   * Asegúrate de marcar **"Imprimir gráficos de fondo"** (para conservar los colores verde/azul de la línea de tiempo).
   * Elige **Guardar como PDF** si deseas compartir la ficha por WhatsApp en las reuniones semanales.
