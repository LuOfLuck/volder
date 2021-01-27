from django.shortcuts import redirect
class RequiredUserAttribute:
    """If the user does not have the specified attribute, it is redirected to the indicated url"""

    def __init__(self, attribute, redirect_to_url, args_dict_to_redirect = {}):
        self.attribute = attribute
        self.redirect_to_url = redirect_to_url
        self.args_dict_to_redirect = args_dict_to_redirect

        assert isinstance(self.args_dict_to_redirect, dict), 'The "args_dict_to_redirect" attribute must be a dictionary'

    def __call__(self, view):

        def wrapper(request, *args, **kwargs):
            if not hasattr(request.user, self.attribute):
                return redirect(self.redirect_to_url, **self.args_dict_to_redirect)
            
            return view(request, *args, **kwargs)
        
        return wrapper