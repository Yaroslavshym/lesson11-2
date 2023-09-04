from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from app import menu_data
from app.menu_data import menu

router = APIRouter(
    prefix='/web',
    tags=['menu', 'landing'],
)

templates = Jinja2Templates(directory='app/templates')


@router.get('/')
async def get_main_page(request: Request):
    context = {
        'request': request,
    }
    return templates.TemplateResponse(
        'base.html',
        context=context

    )
# @router.get('/menu')
# async def get_menu(request: Request):
#     context = {
#         'request': request,
#         'title': 'Menu',
#         'menu': menu,
#     }
#     return templates.TemplateResponse(
#         'menu.html',
#         context=context
#
#     )

@router.get('/about-us')
async def get_about_us(request: Request):
    context = {
        'request': request,
        'title': 'About us',
        'list': [5, 4, 9],

    }
    return templates.TemplateResponse(
        'about_us.html',
        context=context

    )


@router.post('/menu')
@router.get('/menu')
async def get_menu(request: Request, search_text: str = Form(None)):
    filtered_menu = []
    if search_text:
        for dish in menu_data.menu:
            if search_text.lower() in dish['title'].lower():
                filtered_menu.append(dish)

    context = {
        'request': request,
        'title': f'Search resoults for: {search_text}' if search_text else 'Menu',
        'menu': filtered_menu if search_text else menu_data.menu,
    }

    return templates.TemplateResponse(
        'menu.html',
        context=context,
    )

@router.get('/map')
async def map(request: Request):
    context = {
        'request': request,
        'title': 'Map',
    }

    return templates.TemplateResponse(
        'map.html',
        context=context,
    )



@router.get('/message')
async def message(request: Request):
    context = {
        'request': request,
        'title': 'Send someone message',
    }

    return templates.TemplateResponse(
        'message_to_all.html',
        context=context,
    )