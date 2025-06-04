Documentacin del Proyecto: Sistemas Operativos
1. Descripcin General del Proyecto
Este proyecto es una aplicacion web desarrollada en Django con PostgreSQL, contenida en
Docker.
2. Tecnologias Utilizadas
- Python 3.x
- Django
- PostgreSQL
- Docker y Docker Compose
- HTML/CSS
3. Estructura del Proyecto
ProyectoSistemasOp/
 core/
 dashboard/
 usuarios/
 templates/
 manage.py
 requirements.txt
 Dockerfile
 docker-compose.yml
4. Instalacion Local (Sin Docker)
1. git clone <repo-url>
2. cd ProyectoSistemasOp
3. pip install -r requirements.txt
4. Configurar base de datos en settings.py
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver
8. Despliegue con Docker
9. docker-compose up --build
2. docker-compose exec web python manage.py migrate
3. Acceder en http://localhost:8000
6. Comandos Utiles
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver
7. Pruebas
python manage.py test
8. Consideraciones Finales
- Asegurate de tener Docker instalado.
- Usa archivos .env para configurar variables sensibles.
- Puede integrarse Django REST Framework para una API REST.
9. Funcionalidades Principales del Sistema
App: dashboard
- reporte_list
- reporte_create
- reporte_update
- reporte_delete
- reporte_detail
App: usuarios
- register_view
- login_view
- home_view
- logout_view
