from datetime import datetime
from helper import Helper


class Booking:
    def __init__(self, pax_name, date, itinerary):
        self.pax_name = pax_name
        self.date = datetime.strptime(date, "%b-%d %H:%M %Y")
        self.itinerary = itinerary

    def __repr__(self) -> str:
        return repr({
            "pax_name": self.pax_name,
            "date": self.date.strftime("%b-%d %H:%M %Y"),
            "itinerary": self.itinerary
        })

    def __str__(self) -> str:
        return str(f"Pax name: {self.pax_name}, date: {self.date.strftime('%b-%d %H:%M %Y')}, itinerary: {' -> '.join(self.itinerary)}")

    def __iter__(self):
        for each in self.__dict__.items():
            yield each


class Bookings:
    def __init__(self):
        self.current_bookings = []

    def add_booking(self, pax_name, date, itinerary):
        booking = Booking(pax_name, date, itinerary)
        self.current_bookings.append(booking)

    def list_bookings(self):
        for booking in self.current_bookings:
            print(booking)

    def get_all_bookings(self):
        return self.current_bookings

    def search_booking_before_time(self, date):
        return_val = []
        for booking in self.current_bookings:
            if booking.date < datetime.strptime(date, "%b-%d %H:%M %Y"):
                return_val.append(booking)
        return return_val if return_val else "No booking before the selected date!"

    def search_booking_by_airport(self, airport1, airport2):
        return_val = []
        for booking in self.current_bookings:
            itineraries = booking.itinerary
            if airport1 in itineraries and airport2 in itineraries:
                ap1_idx = itineraries.index(airport1)
                ap2_idx = itineraries.index(airport2)
                if ap1_idx < ap2_idx and ap2_idx - ap1_idx == 1:
                    return_val.append(booking)
        return return_val if return_val else f"No booking with {airport1} and {airport2}"


if __name__ == "__main__":
    bookings = Bookings()

    # NOT PART OF THE ASSIGNMENT!
    # this is only for testing purposes
    helper = Helper()
    data = helper.load_data()
    # load data
    for d in data:
        bookings.add_booking(d["pax_name"], d["date"], d["itinerary"])
    # bookings.list_bookings()
    # end

    print("Add new booking...")
    bookings.add_booking(
        pax_name="Brenda",
        date="Jul-13 12:45 2021",
        itinerary=["BUD", "AMS", "JFK"]
    )
    print("List all bookings:")
    bookings.list_bookings()
    print("Search before time:")
    for booking in bookings.search_booking_before_time("Jun-12 08:09 2020"):
        print(booking)
    print("Search by airport(s):")
    for booking in bookings.search_booking_by_airport("AMS", "LHR"):
        print(booking)
