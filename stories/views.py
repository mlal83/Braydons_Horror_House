from cloudinary.utils import cloudinary_url
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .forms import CommentForm, StoryForm, ReviewForm, ProfileForm
from .models import Story, Profile, Comment, Review
from django.contrib.auth.decorators import login_required

import os

def display_stories(request):
    """
    This view displays all the user stories
    """
    stories = Story.objects.all()
    context = {
        'stories': stories
    }
    return render(request, 'stories/stories.html', context)

class StoryList(ListView):
    """
    This StoryList view Lists the stories in a more user-friendly way where the user
    can click into the story card which expands to the story
    """
    model = Story
    template_name = "stories/stories.html"
    context_object_name = "stories"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the genre form
        context['story_form'] = StoryForm()
        return context

class StoryDetailView(DetailView):
    """
    The storyDetail view retrieves the story, queries the user, counts the number of comments and 
    displays their reviews and provides the option to rate the story 
    """
    model = Story
    template_name = 'stories/stories_detail.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        story = self.get_object()
        user_profile = Profile.objects.filter(user=story.author).first()
        if user_profile:
            context['bio'] = user_profile.bio
            context['website_url'] = user_profile.website_url
            if user_profile.profile_picture_upload:
                context['profile_picture_url'] = cloudinary_url(user_profile.profile_picture_upload.public_id)[0]
            else:
                context['profile_picture_url'] = None

        context['comments'] = story.comments.all().order_by("-created_at")
        context['comment_count'] = story.comments.filter(approved=True).count()
        context['comment_form'] = CommentForm()
        context['review_form'] = ReviewForm()
        context['story_form'] = StoryForm()
        return context

def comment_edit(request, slug, comment_id):
    """
    The comment edit view attempts to update data and sends a message that the comment
    is updated successfully
    """ 
    comment = get_object_or_404(Comment, pk=comment_id)
    # Check if the user is authorized to edit this comment
    if comment.author != request.user:
        # Handle unauthorized access here
        messages.error(request, "You are not authorized to edit this comment.")
        return redirect('home')

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment updated successfully.')
            return redirect('stories_detail', slug=slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'stories/stories_detail.html', {'form': form})

def comment_delete(request, slug, comment_id):
    """
    The comment delete view deletes data and also provides a success message that comment 
    successfully deleted
    """ 
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return redirect('stories_detail', slug=slug)
        
    return redirect('stories_detail', slug=slug)

def edit_profile_form(request):
    """
    The edit profile view attempts to update data on the user profile
    """ 
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})

@login_required
def profile_view(request):
    """
    This view manages the user profile, whether its present or creating a new user
    """ 
    profile, created = Profile.objects.get_or_create(user=request.user)
    stories = Story.objects.filter(author=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'profile': profile, 'stories': stories, 'form': form})

from django.shortcuts import redirect

def submit_comment(request, story_id):
    """
    The submit comment view handles the submission of comments for a particular story
    """
    story = Story.objects.get(pk=story_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment submitted successfully.')
            # Redirect to the homepage after successful comment submission
            return redirect('home')
        else:
            messages.error(request, 'Comment form submission failed. Please check the errors below.')
    else:
        form = CommentForm()

    return render(request, 'submit_comment.html', {'form': form})

@login_required
def submit_story(request):
    """
    The submit story view handles the submission of the story
    """
    if request.method == 'POST':
        story_form = StoryForm(request.POST, request.FILES)
        if story_form.is_valid():
            story = story_form.save(commit=False)
            story.author = request.user
            story.save()
            messages.success(request, 'Story submitted successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Story form submission failed. Please check the errors below.')
    else:
        story_form = StoryForm()

    return render(request, 'stories/stories.html', {'story_form': story_form})

@login_required
def view_profile(request, profile_id):
    """
    Function to view user profile
    """
    profile = get_object_or_404(Profile, id=profile_id) 
    return render(request, 'profile.html', {'profile': profile})


def delete_comment(request, pk, comment_id):
    """
    The comment delete view deletes a comment and redirects to the story detail page.
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if comment.author != request.user:
        messages.error(request, "You are not authorized to delete this comment.")
        return redirect('home') 
    
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return redirect('home', pk=pk)
        
    return redirect('stories_detail', pk=pk)
