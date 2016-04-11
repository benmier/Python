from system.core.model import Model
from flask import Flask, flash, redirect, render_template, session
from datetime import datetime

class Travel(Model):
    def __init__(self):
        super(Travel, self).__init__()
  
    def all_trips(self):
        query = "SELECT destination,start_date,end_date,description,name,user_id,trip_id FROM trips JOIN trips_have_users ON trip_id=user_trip_ids JOIN users on user_id=trip_user_ids ORDER BY start_date desc"
        return self.db.query_db(query)

    def add_trip(self,trip):
        print "#"*50
        print datetime.strptime(trip['start_date'],'%Y-%m-%d')
        errors = []
        if len(trip['destination'])<1 or len(trip['description'])<1 or len(trip['start_date'])<1 or len(trip['end_date'])<1:
            errors.append('No field can be empty')
        if datetime.strptime(trip['start_date'],'%Y-%m-%d').date()<datetime.date(datetime.now()):
            errors.append('Start date cannot be in the past')
        if errors == []:
            query = "INSERT INTO trips (destination,description,start_date,end_date,created_at,updated_at) VALUES (%s,%s,%s,%s,NOW(),NOW())"
            data = [trip['destination'],trip['description'],trip['start_date'],trip['end_date']]
            self.db.query_db(query,data)
            new_trip = self.db.query_db("SELECT * from trips ORDER BY trip_id desc LIMIT 1")
            query2 = "INSERT INTO trips_have_users (trip_user_ids,user_trip_ids) VALUES (%s,%s)"
            data2 = [session['user_id'],new_trip[0]['trip_id']]
            self.db.query_db(query2,data2)
            return new_trip[0]
        else:
            for error in errors:
                flash(error)
            return False;

    def trip_by_id(self,id):
        query = "SELECT destination,start_date,end_date,description,name,user_id,trip_id FROM trips JOIN trips_have_users ON trip_id=user_trip_ids JOIN users on user_id=trip_user_ids WHERE trip_id='{}'".format(id)
        trip = self.db.query_db(query)
        return trip[0]

    def users_by_trip_id(self,id):
        query = "SELECT * FROM users JOIN trips_have_users ON trip_user_ids=user_id WHERE user_trip_ids='{}'".format(id)
        return self.db.query_db(query)

    def join_trip(self,id):
        query = "INSERT INTO trips_have_users (user_trip_ids,trip_user_ids) VALUES (%s,%s)"
        data = [id,session['user_id']]
        return self.db.query_db(query,data)