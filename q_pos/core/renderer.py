import json
from rest_framework.renderers import JSONRenderer


class QuickieRenderer(JSONRenderer):
    """
    This class is to be extended by other custom Renderer
    only the object_name field is required if not provided default object_name is 'objects'

    Example:
        class QuestionRenderer(POSRenderer):
            object_name = 'questions'
    """

    charset = "utf-8"
    object_name = "object"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Implement the render function from the super class JSONRenderer

        :param data: Data from the serializer.
        :param accepted_media_type:
        :param renderer_context:
        :return: Json dump
        :rtype: json
        """

        # If an error occurs delegate JSONRenderer to handle the error
        if data and "errors" in data:
            return super(QuickieRenderer, self).render(data)

        return json.dumps({self.object_name: data})
