
from haystack import indexes
from apps.sample_app.models import SampleModel


class SampleModelIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return SampleModel

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
