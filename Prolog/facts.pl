% Facts about courses in One Piece theme
course(luffy, 'Luffy', 3).
course(zoro, 'Zoro', 4).
course(nami, 'Nami', 3).
course(usopp, 'Usopp', 4).

% Facts about instructors in One Piece theme
instructor(luffy_instructor, 'Monkey D. Luffy', luffy).
instructor(zoro_instructor, 'Roronoa Zoro', zoro).
instructor(nami_instructor, 'Nami', nami).
instructor(usopp_instructor, 'Usopp', usopp).

% Facts about students in One Piece theme
student(luffy_student, 'Luffy').
student(zoro_student, 'Zoro').
student(nami_student, 'Nami').
student(usopp_student, 'Usopp').

% Graduate Stuedent Relationship in One Piece theme
graduate_student(StudentName) :-
    student(StudentName, _).

% Defining faculty as a subclass of instructors in One Piece theme
faculty(InstructorName) :-
    instructor(InstructorName, _, _).
