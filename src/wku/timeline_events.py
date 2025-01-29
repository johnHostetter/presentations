from manim_timeline.timeline_helper import TimelineEvent
from src.oral_proposal.people.zadeh import Zadeh
from src.oral_proposal.people.godel import Godel
from src.oral_proposal.people.einstein import Einstein
from src.oral_proposal.people.max_black import MaxBlack
from src.oral_proposal.people.aristotle import Aristotle
from src.oral_proposal.people.lukasiewicz import Lukasiewicz
from src.oral_proposal.people.plato import PlatoTheoryOfForms
from src.oral_proposal.people.bertrand_russell import BertrandRussell
from src.oral_proposal.timeline_events import make_ww2_slide


def get_short_historical_context() -> list:
    return [
        # dnn_pros_and_cons(),
        # PromptSlide(prompt="Could we have done better?", skip=True),
        # nfn_pros_and_cons(),
        # proposal(),
        # PromptSlide(prompt='But before we begin - what does "fuzzy" mean?', skip=True),
        # # PromptSlide(prompt="And do we even need it?", skip=True),
        # # TimelineEvent(
        # #     start_year=470,
        # #     end_year=399,
        # #     era="Ancient Greece",
        # #     era_notation="BCE",
        # #     event="Socrates",
        # #     animation=Socrates,
        # # ),
        TimelineEvent(
            start_year=427,
            end_year=348,
            era="Ancient Greece",
            era_notation="BCE",
            event="Plato",
            animation=PlatoTheoryOfForms,
        ),
        TimelineEvent(
            start_year=384,
            end_year=322,
            era="Ancient Greece",
            era_notation="BCE",
            event="Aristotle",
            animation=Aristotle,
        ),
        TimelineEvent(
            start_year=1879,
            end_year=1955,
            poi=1921,  # the year of the quote
            era="Common Era",
            era_notation="CE",
            event="Albert Einstein",
            animation=Einstein,
        ),
        TimelineEvent(
            start_year=1878,
            end_year=1956,
            poi=1921,
            era="Common Era",
            era_notation="CE",
            event="Jan Łukasiewicz",
            animation=Lukasiewicz,
        ),
        TimelineEvent(
            start_year=1872,
            end_year=1970,
            poi=1923,  # the year of the quote (Vagueness)
            era="Common Era",
            era_notation="CE",
            event="Bertrand Russell",
            animation=BertrandRussell,
        ),
        TimelineEvent(
            start_year=1906,
            end_year=1978,
            poi=1932,  # Gödel-Dummett logic
            era="Common Era",
            era_notation="CE",
            event="Kurt Gödel",
            animation=Godel,
        ),
        TimelineEvent(
            start_year=1909,
            end_year=1988,
            poi=1937,
            era="Common Era",
            era_notation="CE",
            event="Max Black",
            animation=MaxBlack,
        ),
        make_ww2_slide(
            "germans_in_poland_1939",
            1939,
            caption="Nazi Germany invades Poland (September 1, 1939).",
        ),
        TimelineEvent(
            start_year=1921,
            end_year=2017,
            poi=1965,
            era="Common Era",
            era_notation="CE",
            event="Lotfi A. Zadeh",
            animation=Zadeh,
        ),
    ]
