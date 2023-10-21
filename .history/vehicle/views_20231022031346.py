from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from django_filters import rest_framework as filters
from datetime import timedelta, timezone, datetime
from django.db.models import Q
from .models import Vehicle
from django import template
from selenium import webdriver
import time
import os
import shutil
import urllib.parse


def index(request):
    vehicles = Vehicle.objects.order_by('-list_date').filter(is_published=True)
    vehicles_counter = Vehicle.objects.all().filter(is_published=True).count()
    paginator = Paginator(vehicles, 3)
    page = request.GET.get('page')
    paged_vehicles = paginator.get_page(page)

    context = {
        'vehicles': paged_vehicles,
        'vehicles_counter': vehicles_counter,
    }

    return render(request, 'vehicles/index.html', context)


def vehicles(request):
    vehicles = Vehicle.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(vehicles, 15)
    page = request.GET.get('page')
    paged_vehicles = paginator.get_page(page)

    foo = 123
    bar = 456
    # import pdb; pdb.set_trace()
    # breakpoint()


    context = {
        'vehicles': paged_vehicles,
    }

    return render(request, 'vehicles/vehicles.html', context)


def vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    vehicles_counter = Vehicle.objects.all().filter(is_published=True).count()
    # breakpoint()

    context = {
        'vehicle': vehicle,
        'vehicles_counter': vehicles_counter,
    }

    return render(request, 'vehicles/vehicle.html', context)


def search_vehicles(request):
    queryset_list = Vehicle.objects.order_by('-list_date').filter(is_published=True)
    vehicles_counter = Vehicle.objects.all().filter(is_published=True).count()

    if 'keywords' in request.GET and request.GET['keywords']:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
            Q(model_num__icontains=keywords) |
                Q(name__icontains=keywords) |
                Q(maker__icontains=keywords) |
                Q(body_type__icontains=keywords) |
                Q(body_color__icontains=keywords) |
                Q(car_age__icontains=keywords) |
                Q(vin__icontains=keywords) |
                Q(frame_num__icontains=keywords) |
                Q(price__icontains=keywords)
            ).distinct()


        paginator = Paginator(queryset_list, 15)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        get_dict_copy = request.GET.copy()
        params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()

    context = {
            'page_obj': page_obj,
            'params': params,
            'vehicles_counter': vehicles_counter,
    }
    return render(request, 'vehicles/search_vehicles.html', context)


def scrape(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--lang=ja')
    browser = webdriver.Chrome(chrome_options=options,
                            executable_path='../chromedriver')
    url = "https://motorz-garage.com/parts/"

    PAGER_NEXT = "li.select-page.arrow a[rel='next']"
    POSTS = ".product-item-list__item"
    PRODUCT_NAME = ".product-item-list__item-name"
    IMAGE = ".product-item-list__item-image img"
    PRICE = ".product-item-list__item-price"
    CATEGORY = ".product-item-list__item-category"
    CAR = ".product-item-list__item-car-name"

    browser.get(url)
    while True:  # continue until getting the last page
        if len(browser.find_elements_by_css_selector(PAGER_NEXT)) > 0:
            print("Starting to get posts...")
            posts = browser.find_elements_by_css_selector(POSTS)  # ページ内のタイトル複数
            print(len(posts))
            for post in posts:
                try:
                    new_parts = Part()
                    print(new_parts)
                    name = post.find_element_by_css_selector(PRODUCT_NAME).text
                    new_parts.name = name
                    print(new_parts.name)
                    thumnailURL = post.find_element_by_css_selector(
                        IMAGE).get_attribute("src")
                    new_parts.image = thumnailURL
                    print(new_parts.image)
                    price = post.find_element_by_css_selector(PRICE).text
                    yen = '円'
                    print(yen)
                    newPrice = price.replace(",", "")
                    finalPrice = newPrice.strip(yen)
                    print(finalPrice)
                    new_parts.price = int(finalPrice)
                    print(new_parts.price)
                    category = post.find_element_by_css_selector(CATEGORY).text
                    new_parts.category = category
                    print(new_parts.category)
                    car = post.find_element_by_css_selector(CAR).text
                    new_parts.cars = car
                    print(new_parts.cars)
                    new_parts.save()
                except Exception as e:
                    print(e)
            btn = browser.find_element_by_css_selector(PAGER_NEXT).get_attribute('href')
            print("next url:{}".format(btn))
            time.sleep(3)
            browser.get(btn)
            print("Moving to next page......")
        else:
            print("no pager exist anymore")
            break
            return redirect('/')


