class DatabaseRouter:
    """
    Router para dirigir apps específicas a bases de datos específicas
    """
    
    route_app_labels = {
        'usuarios': 'default',
        'dashboard': 'dashboard',
        'auth': 'default',
        'contenttypes': 'default',
        'sessions': 'default',
        'admin': 'default',
    }

    def db_for_read(self, model, **hints):
        """Sugiere la base de datos desde la que se debe leer."""
        if model._meta.app_label in self.route_app_labels:
            return self.route_app_labels[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """Sugiere la base de datos en la que se debe escribir."""
        if model._meta.app_label in self.route_app_labels:
            return self.route_app_labels[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Permite relaciones si los modelos están en la misma app."""
        db_set = {'default', 'dashboard'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'dashboard':
            return app_label == 'dashboard'
        elif db == 'default':
            return True
        return False

