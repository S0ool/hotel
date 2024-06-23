from django.urls import path
from main_app.views import index, booking, rooms, add_room, delete_room, edit_room_page, edit_room, add_booking, \
    delete_booking, edit_booking, edit_booking_page, add_booking_page

urlpatterns = [
    path('', index, name='index'),
    path('rooms', rooms, name='rooms_page'),
    path('add_room', add_room, name='add_room'),
    path('delete_room', delete_room, name='delete_room'),
    path('edit_room/<int:room_id>', edit_room_page, name='edit_room_page'),
    path('edit_room', edit_room, name='edit_room'),


    path('add_booking', add_booking, name='add_booking'),
    path('add_booking/<int:room_id>', add_booking_page, name='add_booking_page'),
    path('delete_booking', delete_booking, name='delete_booking'),
    path('edit_booking/<int:booking_id>', edit_booking_page, name='edit_booking_page'),
    path('edit_booking', edit_booking, name='edit_booking'),
    path('booking', booking, name='booking_page'),
]
