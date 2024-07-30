from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from book.models import Book
import json


# Create your views here.
def index(request: HttpRequest):
    """

    :param request:HttpRequest
    :return: 渲染后的模板
    """
    # 获取数据
    books = Book.objects.all()
    # 添加js模板
    context = {
        "books": books
    }

    return render(request, "index.html", context)


def favicon(request: HttpRequest):
    """

    :param request:HttpRequest
    :return: 图标视图
    """
    with open('static/favicon.ico', 'rb') as f:
        return HttpResponse(f.read(), content_type='image/vnd.microsoft.icon')


def test_api(request: HttpRequest, id_1, id_2):
    print(request.GET.getlist(key='string'))
    print(request.GET['string'])
    print(id_1, id_2)
    # 获取数据
    books = Book.objects.all()
    print(books)
    # 创建一个只包含书籍名称的列表[字典]
    books_data = [{"name": book.name} for book in books]

    # 将列表转换为JSON字符串
    # json_data = json.dumps(books_data, indent=4)
    json_data = json.dumps(books_data)

    # 打印或返回美化后的JSON字符串
    print(json_data)

    print(request.POST)
    print(request.body.decode())
    # 使用JsonResponse来返回JSON数据
    return JsonResponse(books_data, safe=False)
