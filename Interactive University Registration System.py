from abc import ABC, abstractmethod


# =========================
# Requirement 1: Blueprint
# =========================
class Course(ABC):
    def __init__(self, course_id, name, credit_hours, base_fee):
        self.__course_id = course_id
        self.__name = name
        self.__credit_hours = credit_hours
        self.__base_fee = base_fee

    # Protected getters/setters (Requirement 3: Data Protection)
    def get_id(self):
        return self.__course_id

    def get_name(self):
        return self.__name

    def get_credit_hours(self):
        return self.__credit_hours

    def set_credit_hours(self, value):
        if value > 0:
            self.__credit_hours = value
        else:
            print("Invalid credit hours!")

    def get_base_fee(self):
        return self.__base_fee

    def set_base_fee(self, value):
        if value >= 0:
            self.__base_fee = value
        else:
            print("Invalid fee!")

    # Abstract methods (Blueprint enforcement)
    @abstractmethod
    def calculate_tuition(self):
        pass

    @abstractmethod
    def display_course_info(self):
        pass


# =========================
# Requirement 2: Specialization A (Lab Course)
# =========================
class LabCourse(Course):
    def __init__(self, course_id, name, credit_hours, base_fee, lab_fee):
        super().__init__(course_id, name, credit_hours, base_fee)
        self.lab_fee = lab_fee

    def calculate_tuition(self):
        return self.get_base_fee() + self.lab_fee

    def display_course_info(self):
        return f"[Lab] {self.get_id()} - {self.get_name()} | Credit Hours: {self.get_credit_hours()} | Lab Fee: {self.lab_fee}"


# =========================
# Requirement 2: Specialization B (Lecture Course)
# =========================
class LectureCourse(Course):
    def __init__(self, course_id, name, credit_hours, base_fee, online: bool):
        super().__init__(course_id, name, credit_hours, base_fee)
        self.online = online

    def calculate_tuition(self):
        if self.online:
            return self.get_base_fee() * 1.05  # 5% tech fee
        return self.get_base_fee()

    def display_course_info(self):
        mode = "Online" if self.online else "On-Campus"
        return f"[Lecture] {self.get_id()} - {self.get_name()} | Credit Hours: {self.get_credit_hours()} | Mode: {mode}"


# =========================
# Requirement 4: Student Schedule
# =========================
class StudentSchedule:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"{course.get_name()} added successfully.")

    def view_courses(self):
        if not self.courses:
            print("No courses registered.")
            return
        for c in self.courses:
            print(c.display_course_info())

    def calculate_total_tuition(self):
        total = 0
        for c in self.courses:
            total += c.calculate_tuition()
        return total


# =========================
# Sample Course Data
# =========================
courses = [
    LectureCourse("CS101", "Intro to Programming", 3, 1000, True),
    LectureCourse("MATH201", "Calculus I", 4, 1200, False),
    LabCourse("CS102L", "Programming Lab", 1, 500, 150),
    LabCourse("PHY110L", "Physics Lab", 1, 600, 200),
]

schedule = StudentSchedule()


# =========================
# Requirement 5: Terminal App
# =========================
def show_courses():
    print("\nAvailable Courses:")
    for c in courses:
        print(c.display_course_info())


def find_course(course_id):
    for c in courses:
        if c.get_id().lower() == course_id.lower():
            return c
    return None


def main():
    while True:
        print("\n===== University Registration System =====")
        print("1. View Courses")
        print("2. Register for Course")
        print("3. View My Schedule")
        print("4. Print Tuition Bill")
        print("5. Exit")

        choice = input("Enter choice: ")

        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        choice = int(choice)

        if choice == 1:
            show_courses()

        elif choice == 2:
            course_id = input("Enter Course ID: ")
            course = find_course(course_id)
            if course:
                schedule.add_course(course)
            else:
                print("Course not found.")

        elif choice == 3:
            schedule.view_courses()

        elif choice == 4:
            total = schedule.calculate_total_tuition()
            print("\n===== Tuition Receipt =====")
            schedule.view_courses()
            print(f"\nTotal Tuition: {total} EGP")

        elif choice == 5:
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
