# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image eclipse_1 = "eclipse_1.jpg"
define teacher = Character("Robot Teacher", image="teacher")
image teacher = "robot_teacher.png"
image you_lost = "you_lost.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eclipse_1
    show teacher at right
    # These display lines of dialogue.
    label .first_question:
    "First question: When you look up into the sky and witness an exlipse, do you know how this phenomenon occurs?"
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

    label .lost_screen:
    scene you_lost
    ""

    return
