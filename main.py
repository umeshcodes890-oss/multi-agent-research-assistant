from workflows.research_graph import graph

topic = input("Enter Research Topic: ")

result = graph.invoke({
    "topic": topic
})

print("\n")
print("=" * 60)
print("FINAL REPORT")
print("=" * 60)
print(result["report"])