import unittest
from classes.guests import Guests
from classes.songs import Songs
from classes.bar import Bar
from classes.rooms import Rooms

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.capacity = 5
        self.entry_fee = 10
        self.song_selection = []
        self.rooms = Rooms(self.capacity, self.entry_fee)
        self.songs = Songs()
        self.guests = Guests()
       
        
    def test_room_song_list_can_be_populated(self):
        self.songs.add_song_to_selection()

        self.rooms.load_song_selection()

        self.assertEqual(4, self.rooms.room_song_list_length())

    def test_room_guest_list_can_be_populated(self):
        self.rooms.load_guest_list()
        self.assertEqual(3, self.rooms.room_guest_list_length())

    def test_room_guest_list_can_be_cleared(self):
        self.rooms.load_guest_list()
        self.rooms.clear_guest_list()
        self.assertEqual(0, self.rooms.room_guest_list_length())

    def test_room_guests_have_entry_fee_taken(self):
        self.rooms.take_entry_fee_from_guests()
        self.assertEqual(40, self.rooms.room_guest_list[0]['money'])

    def test_room_admin_has_entry_fee_added_to_total_cash_in(self):
        self.rooms.add_entry_fee_to_admin()
        self.assertEqual(30, self.rooms.admin['total_cash_in'])

    def test_room_capacity_has_exceeded_return_no_more_than_5(self):
        self.rooms.load_more_guests()
        self.assertEqual("5 Person Capacity", self.rooms.capacity_past_limit())

    def test_if_customer_cannot_afford_entry_fee_dont_add_to_guestlist(self):
        self.rooms.load_more_guests_with_entry_condition()
        self.assertEqual(7, self.rooms.room_guest_list_length())

    