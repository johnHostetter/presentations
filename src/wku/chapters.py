from manim_timeline.timeline import Timeline

from src.oral_proposal.timeline_events import from_zadeh_to_nfn
from src.wku.timeline_events import get_short_historical_context


class ShortHistory(Timeline):
    """
    Stops at the first NFN publication.
    """

    def __init__(self, **kwargs):
        super().__init__(
            timeline_events=get_short_historical_context() + from_zadeh_to_nfn(),
            incl_ending=False,
            globally_enable_animation=True,
            **kwargs
        )

if __name__ == "__main__":
    ShortHistory().render()
