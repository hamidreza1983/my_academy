from django.shortcuts import render, get_object_or_404, redirect


def maintenance(req):
    return render(req,'maintenance.html')