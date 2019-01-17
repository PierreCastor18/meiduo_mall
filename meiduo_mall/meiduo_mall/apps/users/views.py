from django.shortcuts import render

# Create your views here.

# 测试视图
def test(request):
    return render(request, 'test.html')