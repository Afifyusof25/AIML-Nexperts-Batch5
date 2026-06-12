import requests
import gradio as gr

# ------------------------------
# API FUNCTIONS
# ------------------------------

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    r = requests.get(url).json()
    return f"{r['setup']} ... {r['punchline']}"

def get_advice():
    url = "https://api.adviceslip.com/advice"
    r = requests.get(url).json()
    return r["slip"]["advice"]

def get_quote():
    url = "https://api.quotable.io/random"
    r = requests.get(url).json()
    return f"{r['content']} — {r['author']}"

def get_weather(city="London"):
    url = f"https://wttr.in/{city}?format=3"
    r = requests.get(url).text
    return r

def get_news():
    url = "https://inshortsapi.vercel.app/news?category=technology"
    r = requests.get(url).json()
    article = r["data"][0]
    return f"{article['title']}\n\n{article['content']}"

# ------------------------------
# MAIN GENERATOR FUNCTION
# ------------------------------

def generate(choice, city):
    if choice == "Random Joke":
        return get_joke()
    elif choice == "Random Advice":
        return get_advice()
    elif choice == "Random Quote":
        return get_quote()
    elif choice == "Weather":
        return get_weather(city)
    elif choice == "Tech News":
        return get_news()
    elif choice == "Joke + Advice Combo":
        return f"Joke:\n{get_joke()}\n\nAdvice:\n{get_advice()}"
    else:
        return "Please select an option."

# ------------------------------
# GRADIO UI
# ------------------------------

with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("""
    # 🌐 Multi‑API Text Generator  
    ### Jokes • Advice • Quotes • Weather • News  
    """)

    with gr.Row():
        choice = gr.Dropdown(
            ["Random Joke", "Random Advice", "Random Quote", "Weather", "Tech News", "Joke + Advice Combo"],
            label="Choose API"
        )
        city = gr.Textbox(label="City (for weather)", value="London")

    output = gr.Textbox(label="API Result", lines=10)

    with gr.Row():
        btn = gr.Button("Generate")
        refresh = gr.Button("Refresh 🔄")

    btn.click(generate, inputs=[choice, city], outputs=output)
    refresh.click(generate, inputs=[choice, city], outputs=output)

app.launch()

