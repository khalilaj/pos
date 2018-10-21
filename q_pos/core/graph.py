from graphene import relay


class RelayNode(relay.Node):

    # remove graphene base64 ID and returns the original ID
    @classmethod
    def get_node_from_global_id(cls, info, global_id, only_type=None):

        node = super().get_node_from_global_id(info, global_id, only_type=None)
        if node:
            return node

        get_node = getattr(only_type, "get_node", None)
        if get_node:
            return get_node(info, global_id)

    @classmethod
    def to_global_id(cls, type, id):
        return id
