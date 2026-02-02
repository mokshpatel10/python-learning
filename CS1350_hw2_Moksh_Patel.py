# Prob 1
# Part A

ratings = {
    "Alice": {"Inception": 5, "Titanic": 3, "Avatar": 4, "Jaws": 2},
    "Bob": {"Inception": 4, "The Matrix": 5, "Avatar": 5, "Jaws": 3},
    "Carol": {"Titanic": 5, "The Matrix": 4, "Avatar": 3, "Interstellar": 5},
    "Dave": {"Inception": 3, "Titanic": 4, "The Matrix": 5, "Jaws": 4},
    "Eve": {"Inception": 5, "Avatar": 4, "Interstellar": 4, "Jaws": 1}
}

print("\n=== User Statistics ===")
for user, movies in ratings.items():
    num_movies = len(movies)
    
    total_rating = sum(movies.values())
    avg_rating = total_rating/num_movies
    
    max_rating = max(movies.values())
    favorite_movie = None
    for movie, rating in movies.items():
        if rating == max_rating:
            favorite_movie = movie
            break
        
    print(f"{user}: {num_movies} movies, avg rating: {avg_rating:.2f}, favorite: {favorite_movie} ({max_rating})")
    
#Part B

movie_stats = {}

for user, movies in ratings.items():
    for movie, rating in movies.items():
        if movie not in movie_stats:
            movie_stats[movie] = {
                "ratings": [],
                "avg": 0,
                "count": 0
            }
        
        movie_stats[movie]["ratings"].append(rating) 

for movie, stats in movie_stats.items():
    stats["count"] = len(stats["ratings"])
    stats["avg"] = sum(stats["ratings"]) / stats["count"]

print("\n=== Movie Statistics ===")

sorted_movies = sorted(movie_stats.items(), key=lambda x: (-x[1]["avg"], x[0]))

for movie, stats in sorted_movies:
    print(f"{movie}: {stats['avg']:.2f} avg ({stats['count']} reviews)")
    
#Part C

high_rated_movies = []

for movie, stats in movie_stats.items():
    if stats["avg"] >= 4.0:
        high_rated_movies.append(movie)

alice_rated = ratings["Alice"].keys()  
recommendations = []

for movie in high_rated_movies:
    if movie not in alice_rated:
        recommendations.append(movie)

print("\n=== Recommendations for Alice ===")
for movie in recommendations:
    print(f"{movie}: {movie_stats[movie]['avg']:.2f} avg")

# Prob 2
# Part A

sales_records = [
    {"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 5,
     "region": "North"},
    {"product": "Mouse", "category": "Electronics", "price": 25, "quantity": 50,
     "region": "North"},
    {"product": "Desk", "category": "Furniture", "price": 350, "quantity": 8,
     "region": "South"},
    {"product": "Chair", "category": "Furniture", "price": 150, "quantity": 20,
     "region": "South"},
    {"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 3,
     "region": "South"},
    {"product": "Keyboard", "category": "Electronics", "price": 75, "quantity": 30,
     "region": "North"},
    {"product": "Desk", "category": "Furniture", "price": 350, "quantity": 5,
     "region": "North"},
    {"product": "Monitor", "category": "Electronics", "price": 300, "quantity": 12,
     "region": "South"},
]

product_prices = {record["product"]: record["price"] for record in sales_records}

expensive_products = {record["product"]: record["price"] for record in sales_records if record["price"] > 100}

price_category = {record["product"]: "Premium" if record["price"] >= 300 else "Standard" for record in sales_records}

print("\n=== Part A: Comprehensions ===")
print(f"Product prices: {product_prices}")
print(f"Expensive products (>$100): {expensive_products}")
print(f"Price categories: {price_category}")

# Part B

total_by_category = {}
for record in sales_records:
    category = record["category"]
    revenue = record["price"] * record["quantity"]
    total_by_category[category] = total_by_category.get(category, 0) + revenue

total_by_region = {}
for record in sales_records:
    region = record["region"]
    revenue = record["price"] * record["quantity"]
    total_by_region[region] = total_by_region.get(region, 0) + revenue

quantity_by_product = {}
for record in sales_records:
    product = record["product"]
    quantity = record["quantity"]
    quantity_by_product[product] = quantity_by_product.get(product, 0) + quantity

print("\n=== Part B: Aggregations ===")
print(f"Revenue by category: {total_by_category}")
print(f"Revenue by region: {total_by_region}")
print(f"Quantity by product: {quantity_by_product}")

# Prob 3

registrations = {
    "Alice": {"CS101", "CS201", "MATH101"},
    "Bob": {"CS101", "MATH101", "PHYS101"},
    "Carol": {"CS201", "CS301", "MATH201"},
    "Dave": {"CS101", "CS201", "MATH101", "PHYS101"},
    "Eve": {"CS301", "MATH201", "MATH301"}
}

prerequisites = {
    "CS101": set(),
    "CS201": {"CS101"},
    "CS301": {"CS201"},
    "MATH101": set(),
    "MATH201": {"MATH101"},
    "MATH301": {"MATH201"},
    "PHYS101": {"MATH101"}
}

capacity = {
    "CS101": 30, "CS201": 25, "CS301": 20,
    "MATH101": 35, "MATH201": 25, "MATH301": 20, "PHYS101": 30
}

print("\n=== Part A: Set Operations ===")

all_courses = set()
for student, courses in registrations.items():
    all_courses = all_courses.union(courses)
print(f"All courses with enrollment: {all_courses}")

common_courses = set(registrations["Alice"])
for student, courses in registrations.items():
    common_courses = common_courses.intersection(courses)
print(f"Courses ALL students share: {common_courses}")

alice_only = set(registrations["Alice"])
for student, courses in registrations.items():
    if student != "Alice":
        alice_only = alice_only - courses
print(f"Courses ONLY Alice takes: {alice_only}")

cs_students = set()
for student, courses in registrations.items():
    for course in courses:
        if course.startswith("CS"):
            cs_students.add(student)
            break
print(f"Students in CS courses: {cs_students}")

print("\n=== Part B: Prerequisite Check ===")

def get_all_prerequisites(course, prereqs):
    """Recursively get ALL prerequisites for a course (including nested)"""
    all_prereqs = set()
    direct_prereqs = prereqs.get(course, set())
    
    for prereq in direct_prereqs:
        all_prereqs.add(prereq)
        # Recursively add prerequisites of prerequisites
        all_prereqs.update(get_all_prerequisites(prereq, prereqs))
    
    return all_prereqs

for student, courses in registrations.items():
    valid = True
    missing_info = []
    
    for course in courses:
        # Get ALL prerequisites (direct + nested)
        all_required = get_all_prerequisites(course, prerequisites)
        missing = all_required - courses
        
        if missing:
            valid = False
            # Show direct prerequisite but list ALL missing
            direct_prereq = prerequisites.get(course, set())
            missing_info.append(f"{course} requires {direct_prereq} but missing: {missing}")
    
    if valid:
        print(f"{student}: VALID")
    else:
        print(f"{student}: INVALID")
        print("  - Missing prerequisites:")
        for info in missing_info:
            print(f"  {info}")

print("\n=== Part C: Enrollment Analysis ===")

overloaded = {student for student, courses in registrations.items() if len(courses) >= 4}
print(f"Overloaded students (4+ courses): {overloaded}")

math_courses = set()
for student, courses in registrations.items():
    for course in courses:
        if course.startswith("MATH"):
            math_courses.add(course)
print(f"All MATH courses enrolled: {math_courses}")

identical_found = False
students_list = list(registrations.keys())
print("Students with identical schedules: ", end="")

for i in range(len(students_list)):
    for j in range(i + 1, len(students_list)):
        student1 = students_list[i]
        student2 = students_list[j]
        if registrations[student1] == registrations[student2]:
            print(f"{student1} and {student2}", end=" ")
            identical_found = True

if not identical_found:
    print("None found")
else:
    print()

print("Enrollment per course:")
enrollment_count = {}

for student, courses in registrations.items():
    for course in courses:
        enrollment_count[course] = enrollment_count.get(course, 0) + 1

for course in sorted(enrollment_count.keys()):
    print(f"  {course}: {enrollment_count[course]} students")

under_enrolled = {course for course, count in enrollment_count.items() if count < 3}
print(f"Under-enrolled courses (<3 students): {under_enrolled}")