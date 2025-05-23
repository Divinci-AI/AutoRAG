import pandas as pd

passage1 = """Filename: New Jeans never die.
NewJeans (뉴진스) is a 5-member girl group under ADOR and HYBE Labels.
The members consist of Minji, Hanni, Danielle, Haerin, and Hyein.
They released their debut single “Attention” on July 22, 2022,
followed by their debut extended play, New Jeans, which was released on August 1, 2022."""
passage2 = """The digital age has transformed the way we live, work, and interact, bringing both opportunities and challenges.
With the rise of artificial intelligence, automation, and data-driven technologies, industries are evolving at an unprecedented pace.
While these advancements enhance efficiency and innovation,
they also raise ethical concerns around privacy, employment, and the role of human decision-making."""

qa_df = pd.DataFrame(
    {
        "qid": ["jax1", "jax2"],
        "retrieval_gt": [[["havertz1"]], [["havertz2"]]],
        "retrieval_gt_contents": [
            [[passage1]],
            [[passage2]],
        ],
    }
)


multi_hop_qa_df = pd.DataFrame(
    {
        "qid": ["jax1"],
        "retrieval_gt": [[["havertz1"], ["havertz2"]]],
        "retrieval_gt_contents": [
            [[passage1], [passage2]],
        ],
    }
)
