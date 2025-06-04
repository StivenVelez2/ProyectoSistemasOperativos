from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reporte
from .forms import ReporteForm

@login_required
def reporte_list(request):
    reportes = Reporte.objects.using('dashboard').filter(usuario_id=request.user.id)
    return render(request, 'dashboard/reporte_list.html', {'reportes': reportes})

@login_required
def reporte_create(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.usuario_id = request.user.id
            reporte.save(using='dashboard')
            return redirect('dashboard:reporte_list')
    else:
        form = ReporteForm()
    return render(request, 'dashboard/reporte_form.html', {'form': form})

@login_required
def reporte_update(request, pk):
    reporte = get_object_or_404(Reporte.objects.using('dashboard'), pk=pk, usuario_id=request.user.id)
    if request.method == 'POST':
        form = ReporteForm(request.POST, instance=reporte)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.save(using='dashboard')
            return redirect('dashboard:reporte_list')
    else:
        form = ReporteForm(instance=reporte)
    return render(request, 'dashboard/reporte_form.html', {'form': form})

@login_required
def reporte_delete(request, pk):
    reporte = get_object_or_404(Reporte.objects.using('dashboard'), pk=pk, usuario_id=request.user.id)
    if request.method == 'POST':
        reporte.delete(using='dashboard')
        return redirect('dashboard:reporte_list')
    return render(request, 'dashboard/reporte_confirm_delete.html', {'reporte': reporte})

@login_required
def reporte_detail(request, pk):
    reporte = get_object_or_404(Reporte.objects.using('dashboard'), pk=pk, usuario_id=request.user.id)
    return render(request, 'dashboard/reporte_detail.html', {'reporte': reporte})
