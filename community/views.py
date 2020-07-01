from django.shortcuts import render
from django.views.generic import ListView, DetailView
from community.models import Community
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from config.views import OwnerOnlyMixin


class CommunityLV(ListView):
    model = Community

class CommunityDV(DetailView):
    model = Community

class CommunityCreateView(LoginRequiredMixin, CreateView):
    model = Community
    fields = ['title','url']
    success_url = reverse_lazy('community:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CommunityChangeLV(LoginRequiredMixin, ListView):
    template_name = 'community/community_change_list.html'

    def get_queryset(self):
        return Community.objects.filter(owner=self.request.user)

class CommunityUpdateView(OwnerOnlyMixin, UpdateView):
    model = Community
    fields = ['title','url']
    success_url = reverse_lazy('community:index')

class CommunityDeleteView(OwnerOnlyMixin, DeleteView):
    model = Community
    success_url = reverse_lazy('community:index')

# Create your views here.
