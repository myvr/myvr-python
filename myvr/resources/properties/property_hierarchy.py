from myvr.api.mixins import ListMixin


class PropertyHierarchy(ListMixin):
    resource_url = '/property-hierarchy/'
    model_name = 'Property Hierarchy'
