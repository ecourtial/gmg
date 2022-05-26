class RessourceHasChildrenException(Exception):
    """Raised when the resource has children, for instance a version of a game has stories"""
    def __init__(self, resource_type, child_type):
        super().__init__(f"The following resource type '{resource_type}' has children of type '{child_type}', so it cannot be deleted.")
