from django.conf.urls import url, include
from . import views
# . means importing from current directory
# https://stackoverflow.com/a/28316021 = how to use API with CSRF token

urlpatterns = [
    url(r'^$', views.index, name='index'), # This is the base index for .../api/

    url(r'^register', include('knowItAllAPI.register.urls')), # This is .../api/register
    url(r'^authenticate', include('knowItAllAPI.authenticate.urls')),
    url(r'^editProfile', include('knowItAllAPI.editProfile.urls')),

    url(r'^createCategory', include('knowItAllAPI.createCategory.urls')),
    url(r'^createPoll', include('knowItAllAPI.createPoll.urls')),
    url(r'^createTopic', include('knowItAllAPI.createTopic.urls')),
    url(r'^createReview', include('knowItAllAPI.createReview.urls')),
    url(r'^createNotification', include('knowItAllAPI.createNotification.urls')),
    url(r'^vote', include('knowItAllAPI.vote.urls')),

    url(r'^myPosts', include('knowItAllAPI.myPosts.urls')),
    url(r'^getPost', include('knowItAllAPI.getPost.urls')),
    url(r'^editPost', include('knowItAllAPI.editPost.urls')),
    url(r'^getTrending', include('knowItAllAPI.getTrending.urls')),

    url(r'^myNotifications', include('knowItAllAPI.myNotifications.urls')),
    url(r'^search', include('knowItAllAPI.search.urls')),

    url(r'^deletePoll', include('knowItAllAPI.deletePoll.urls')),
    url(r'^deleteReview', include('knowItAllAPI.deleteReview.urls')),
]