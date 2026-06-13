import arxiv

def academic_agent(state):

    print("Running Academic Agent...")

    topic = state["topic"]

    papers = []

    try:

        search = arxiv.Search(
            query=topic,
            max_results=5,
            sort_by=arxiv.SortCriterion.Relevance
        )

        for paper in search.results():

            papers.append(
                f"""
TITLE:
{paper.title}

SUMMARY:
{paper.summary[:1000]}

AUTHORS:
{', '.join([str(a) for a in paper.authors])}

URL:
{paper.entry_id}
"""
            )

    except Exception as e:

        print("Arxiv Error:", e)

    return {
        "academic_sources": "\n\n".join(papers)
    }