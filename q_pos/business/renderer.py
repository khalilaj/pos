from ..core.renderer import QuickieRenderer


class BusinessRenderer(QuickieRenderer):
    """Extends QuickieRenderer only the object_name field is defined
    Fields:
        object_name: The name of object to be rendered
    """
    object_name = 'business'
