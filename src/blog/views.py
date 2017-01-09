# All the imports
from logging import getLogger

from blog.models import *
from django.views.generic import ListView, DetailView, FormView

from blog.forms import ContactForm

logger = getLogger("blog")


# Custom Mixin
class PublishedMixin(object):
    def get_queryset(self):
        return self.model.objects.get_queryset()


# All the views are defined lexicographically
class AboutView(ListView):
    model = About
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        try:
            context['about_image'] = list(Image.objects.values('about_image')[0].values())[0]
        except IndexError as e:
            logger.error("Error occurred in [{}]: [{}]".format(self.__class__.__name__, e))
            pass
        return context


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = 'thanks/'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        try:
            image = Image.objects.values('contact_image')
            if image.count() > 0:
                context['contact_image'] = list(image[0].values())[0]
        except IndexError as e:
            logger.error("Error occurred in [{}]: [{}]".format(self.__class__.__name__, e))
            pass
        return context

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)


class IndexView(PublishedMixin, ListView):
    model = Post
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        try:
            # Add in a QuerySet of all the books
            last = Project.objects.all().count()
            context['project_list'] = Project.objects.exclude(id=Project.objects.latest('date').id, ).order_by(
                '-date')
            context['work_list'] = Work.objects.all()
            context['latest'] = Project.objects.latest('date')
            context['about_list'] = About.objects.all()[:3]
            context['skill_list'] = Skill.objects.all()
            context['education_list'] = Education.objects.all()
            context['music_list'] = Music.objects.all()
            context['userdata'] = UserData.objects.get(pk=1)
            context['language_list'] = Language.objects.all()
            context['conference_list'] = Conference.objects.all()
        except Exception as e:
            logger.error("Error occurred in [{}]: [{}]".format(self.__class__.__name__, e))
            pass

        return context


class PostDetailView(PublishedMixin, DetailView):
    model = Post
    template_name = "blog/blog_post.html"


class PostListView(PublishedMixin, ListView):
    model = Post
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        try:
            context['postlist_image'] = list(Image.objects.values('postlist_image')[0].values())[0]
        except IndexError as e:
            logger.error("Error occurred in [{}]: [{}]".format(self.__class__.__name__, e))
            pass
        return context


class ProjectDetailView(PublishedMixin, DetailView):
    model = Project
    template_name = "blog/project_detail.html"


class ProjectListView(PublishedMixin, ListView):
    model = Project
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        try:
            context['projectlist_image'] = list(Image.objects.values('projectlist_image')[0].values())[0]
        except IndexError as e:
            logger.error("Error occurred in [{}]: [{}]".format(self.__class__.__name__, e))
            pass
        return context


class TagListView(ListView):
    models = Tag
    paginate_by = 5
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            tag = Tag.objects.get(slug=slug)
            results = Post.objects.filter(tags=tag)
            return results
        except Tag.DoesNotExist as e:
            logger.error("Error occurred in [{}]: [{}]".format(self.__class__.__name__, e))
            return None
