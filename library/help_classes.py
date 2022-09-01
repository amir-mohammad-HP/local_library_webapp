class common_template:
    # manage built in paginator
    paginate_by = 10
    # make a distinguish between diffrent pages by the view name
    view = None
    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = self.view
        return ctx
    