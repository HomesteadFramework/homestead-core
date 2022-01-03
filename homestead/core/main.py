from fastapi import FastAPI


class Homestead(FastAPI):
    """
    A simple wrapper around FastAPI.
    Use this instead of FastAPI if you want to use the Homestead methods.
    """
    def get(self, *args, **kwargs):
        """Raise not implemented error. Force to use the Homestead routers."""
        raise NotImplementedError("Use the Homestead routers instead.")

    def post(self, *args, **kwargs):
        """Raise not implemented error. Force to use the Homestead routers."""
        raise NotImplementedError("Use the Homestead routers instead.")

    def put(self, *args, **kwargs):
        """Raise not implemented error. Force to use the Homestead routers."""
        raise NotImplementedError("Use the Homestead routers instead.")

    def patch(self, *args, **kwargs):
        """Raise not implemented error. Force to use the Homestead routers."""
        raise NotImplementedError("Use the Homestead routers instead.")

    def delete(self, *args, **kwargs):
        """Raise not implemented error. Force to use the Homestead routers."""
        raise NotImplementedError("Use the Homestead routers instead.")
