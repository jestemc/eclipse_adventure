
define teacher = Character("The Professor", image="teacher")
define student = Character("[student_name]", image="student")
image teacher = im.FactorScale("robot_teacher.png", 1.3)
image teacher big = im.FactorScale("robot_teacher.png", 1.5)
image student = im.FactorScale("silueta_nino.png", 1.3)


image planetarium = "planetarium.jpg"
image inside_planetarium = "inside_planetarium.jpg"
image eclipse_1 = "eclipse_1.jpg"
image eclipse_2 = "eclipse_2.png"
image eclipse_3 = "eclipse_3.jpg"
image eclipse_4 = "eclipse_4.jpg"
image eclipse_5 = "eclipse_5.jpg"
image eclipse_6 = "eclipse_6.jpg"
image eclipse_7 = "eclipse_7.jpg"
image you_lost = "you_lost.png"
image space_station = "space_station.jpg"
image the_end = "the_end.png"

transform pan_up:
    ypos -1300
    linear 8 ypos 0

label start:
    python:
        debug = False
        student_name = renpy.input("What is your name?", length=32) if not debug else ""
        student_name = student_name.strip()

        if not student_name:
            student_name = "Timmy"

    show space_station

    "In the year 2X23, planet Earth has advanced immensely in terms of technology to the point where all buildings are completely controlled by AIs, who have total access to information."

    show planetarium
    "This story presents the journey of a school group to the Great Observatory, an ancient and enormous building filled with books, holograms, and information about the stars."

    show teacher big
    "This old building is managed by The Professor, a robot as old as the building itself, created to learn and understand all the information available in the Great Observatory."
    "This robot is known for being grumpy, demanding, and very impatient."
    hide teacher big

    "This story is centered around [student_name], who along with their classmates, went to the Great Observatory on a school trip."

    scene inside_planetarium at pan_up
    pause 8
    "Inside the Great Observatory, they were greeted rudely by The Professor, who introduced himself with an air of superiority, seeing the group as mere ignorant children."

    show teacher at right
    teacher "Why have you come to MY observatory?"

    show student at left
    student "We heard there would be an eclipse tomorrow! We want to learn more about it!"

    "Those words did not bring particular joy to that robot, who, rather than being excited about the possibility of sharing knowledge with younger minds, saw it as a nuisance. He already knew EVERYTHING, why should he have to teach it?"

    teacher "Is that so?" 
    teacher "You can learn about it in your school; it's a topic your teachers cover, isn't it?" 

    student "But this is the Great Observatory! It has ultra-realistic models, holograms, and more! They say seeing the stars here is like seeing them for real!"

    teacher "Nothing you can't see elsewhere."
    teacher "If you'll excuse me, I have much more important matters that require my immediate attention."

    "The Professor had many things he preferred to do rather than teach those he viewed as uncultured minds."
    "If they wanted to know so badly, there was the school, the teachers, and other AIs for that. It was not his responsibility or desire to teach anyone."

    student "But aren't you The Professor? The one who knows everything humanity knows about the stars and space?"
    student "We asked to come here because it's the best place of all! Can't you spare us a few minutes at least?"

    teacher "As I said before, I'm very busy, child."

    "Despite The Professor's bad attitude, [student_name] decided to insist a little more. Of all the places they could have gone, they chose this one because they wanted to know what would happen tomorrow to appreciate it better, and they didn't plan to leave empty-handed."

    student "Please, the eclipse is tomorrow!"

    # TODO: make more dramatic
    "Fed up, The Professor closed the windows and blocked the exits. If they wanted to know so badly, then it would be on his terms."

    teacher "Let's see how much you know then, child. Let's see if you're worth my time."

    "Turning his back to the children, The Professor approached the first panel and demanded..."

    teacher "No one will go home until you tell me what I want to know."

    show eclipse_1
    show teacher at right
    # These display lines of dialogue.
    label .first_question:
    "First question: When you look up into the sky and witness an eclipse, do you know how this phenomenon occurs?"
    menu: 
        "Due to the Earth's rotation.":
            "Incorrect! Try again."
            jump .first_question
        "When the Sun, Moon, and Earth perfectly align.":
            "Correct!"
        "Because of stars hiding the Moon.":
            "Incorrect! Try again."
            jump .first_question
        "Due to light refraction in the atmosphere.":
            "Incorrect! Try again"
            jump .first_question

    show eclipse_2
    "Second question: If an eclipse is occurring, why can only some Earthlings see it?"
    label .second_question:
    menu:
        "Because the Earth is flat.":
            "Incorrect! Try again."
            jump .second_question
        "Due to clouds blocking the view.":
            "Incorrect! Try again."
            jump .second_question
        "Because it only happens at night.":
            "Incorrect! Try again."
            jump .second_question
        "Because the cast shadow only covers part of the Earth.":
            "Correct!"

    show eclipse_3
    "Third question: What mysterious force causes the Sun, Moon, and Earth to align?"
    label .third_question:
    menu:
        "The magic of the cosmos.":
            "Incorrect! Try again."
            jump .third_question
        "Gravity.":
            "Correct!"
        "Solar wind.":
            "Incorrect! Try again."
            jump .third_question
        "Oceanic tides.":
            "Incorrect! Try again."
            jump .third_question

    show eclipse_4
    "Fourth question: Humans, always observing the sky... How often do eclipses occur?"
    label .fourth_question:
    menu:
        "Once a week.":
            "Incorrect! Try again."
            jump .fourth_question
        "Once a year.":
            "Incorrect! Try again."
            jump .fourth_question
        "Several times a year, but not every month.":
            "Correct!"
        "Every day.":
            "Incorrect! Try again."
            jump .fourth_question

    show eclipse_5
    "Fifth question: Earthly scientists seem to know much. How do they predict when and where eclipses will occur?"
    label .fifth_question:
    menu:
        "By guessing.":
            "Incorrect! Try again."
            jump .fifth_question
        "Watching shooting stars.":
            "Incorrect! Try again."
            jump .fifth_question
        "Using algorithms based on orbits and positions of celestial bodies.":
            "Correct!"
        "Following the phases of the Moon.":
            "Incorrect! Try again."
            jump .fifth_question

    show eclipse_6
    "Sixth question: Prove to me you know the difference. What distinguishes a lunar eclipse from a solar eclipse?"
    label .sixth_question:
    menu:
        "In one, the Moon disappears; in the other, the Sun.":
            "Incorrect! Try again."
            jump .sixth_question
        "In a lunar eclipse, the Moon comes between the Earth and the Sun. In a solar eclipse, it's the Earth that comes between.":
            "Correct!"
        "In a lunar eclipse, the Earth comes between the Sun and the Moon. In a solar eclipse, the Moon comes between the Earth and the Sun.":
            "Incorrect! Try again."
            jump .sixth_question
        "There's no difference; it's just terminology.":
            "Incorrect! Try again."
            jump .sixth_question

    show eclipse_7
    "Seventh and final question: Humans talk about 'eclipse seasons' occurring twice a year. What are they, and why do they happen approximately every six months?"
    label .seventh_question:
    menu:
        "They are periods when more stars are in the sky.":
            "Incorrect! Try again."
            jump .seventh_question
        "They are times of the year when planets are closer to Earth.":
            "Incorrect! Try again."
            jump .seventh_question
        "They are times when the Earth's axial tilt aligns with the Moon's orbit, allowing conditions for eclipses to occur.":
            "Correct!"
        "It's when the Earth is closer to the Sun.":
            "Incorrect! Try again."
            jump .seventh_question

    scene inside_planetary
    show teacher at right
    show student at left

    teacher "Oh, I see the someone is not as foolish as I thought."
    teacher "Seeing you have answered all my questions correctly, you are free to go or explore MY observatory"

    student "Will you answer my questions now?"

    "For a moment The Professor seemed to see right through [student_name]! He felt chills down his spine."

    teacher "I am a very busy AI, but I will grant you a few minutes if you have questions..."

    show the_end

    return
