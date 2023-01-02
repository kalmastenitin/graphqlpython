# To Insert New data Use
````
mutation {
  createCourse(
    id: "7" 
    title: "Joker it's me" 
    instructor: "Donkey"
  ) {
    course {
      id
      title
      instructor
    }
  }
} 
````

# To get all data 
````
{
  getCourse {
    id
    title
    instructor
    publishDate
        }
}
````

# To get data with id
````
{
  getCourse(id: "2") {
    id
    title
    instructor
    publishDate
        }
}
````
# To get paginated results
````
{
  getCourse(first:3, skip:6) {
    id
    title
    instructor
    publishDate
        }
}
````
# Sample Subscription
````
subscription{
  timeOfDay
}
````