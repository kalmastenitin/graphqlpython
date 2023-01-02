from graphene import ObjectType, List, String, Schema, Field, Mutation, Int
from .schema import CourseType
import json, asyncio
import time
from datetime import datetime
from fastapi import APIRouter
import graphene

router = APIRouter()


@router.get("/subscribe")
async def subscribe_to_event():
    subscription = 'subscription {timeOfDay}'
    result = await schema.subscribe(subscription)
    async for item in result:
        print(item.data['timeOfDay'])
    return "success"


class Query(ObjectType):
    course_list = None
    get_course = Field(List(CourseType), id=String(), first=Int(), skip=Int())

    async def resolve_get_course(self, info, id=None, first=None, skip=None, **kwargs):
        with open("./courses.json") as courses:
            course_list = json.load(courses)
        if id:
            for course in course_list:
                if course['id'] == id:
                    return [course]
        if skip:
            course_list = course_list[skip:]
        if first:
            course_list = course_list[:first]
        return course_list


class CreateCourse(Mutation):
    course = Field(CourseType)

    class Arguments:
        id = String(required=True)
        title = String(required=True)
        instructor = String(required=True)

    async def mutate(self, info, id, title, instructor):
        with open("./courses.json", "r+") as courses:
            course_list = json.load(courses)

            for course in course_list:
                if course["id"] == id:
                    raise Exception("course provided id already exists!")

            course_list.append(
                {"id": id, "title": title, "instructor": instructor})
            courses.seek(0)
            json.dump(course_list, courses, indent=2)
        return CreateCourse(course=course_list[-1])


class Mutation(ObjectType):
    create_course = CreateCourse.Field()


data = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]


class Subscription(ObjectType):

    # count = Int(upto=Int())

    # async def subscribe_count(self, info, upto=10):
    #     i = 1
    #     while i < upto:
    #         time.sleep(10)
    #         yield datetime.now().isoformat()
    time_of_day = String()
    async def subscribe_time_of_day(root, info):
        while True:
            yield datetime.now().isoformat()
            await asyncio.sleep(1)

schema = graphene.Schema(Query, Mutation, Subscription)