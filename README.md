# TFG_e-lapse
# Proyecto Django con Python que consume la API de Marvel
Este es un proyecto Django desarrollado en Python que utiliza la API de Marvel para obtener información sobre personajes, cómics y series de Marvel. Proporciona una interfaz web para buscar y mostrar información relacionada con los personajes de Marvel.

# Requisitos previos

- Python (versión 3.10)
- Django (versión 3.x)
- Git 

# Uso del proyecto
El proyecto proporciona una interfaz web simple para buscar y mostrar información de los personajes de Marvel. Puedes realizar las siguientes acciones:

  - Buscar personajes y cómics por nombre utilizando el campo de búsqueda.
  - Ver detalles de un personaje, incluyendo su descripción, cómics asociados, eventos y series en las que aparece.
  - La estructura del proyecto se organiza de la siguiente manera:

    - marvel_api: Contiene la lógica de la API de Marvel, incluyendo la autenticación y los métodos para consumir los endpoints.
    - characters: Aplicación Django principal para la gestión de los personajes y sus vistas.
    - templates: Contiene las plantillas HTML para las páginas web.
    - static: Directorio para archivos estáticos como CSS o JavaScript.
    - manage.py: Archivo de gestión del proyecto Django.
