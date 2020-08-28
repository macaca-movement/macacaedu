from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Activity


@login_required
def index(request):
    activities = Activity.objects.all()

    context = {
        'activities': activities
    }
    return render(request, 'study/index.html', context)


@login_required
def activity(request, id):
    activity = get_object_or_404(Activity, pk=id)

    context = {
        'activity': activity
    }
    return render(request, 'study/activity.html', context)
