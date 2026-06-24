# model loader placeholder
"""
LLM Loader
Loads open-source Hugging Face models
"""

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline
)

SUPPORTED_MODELS = {
    "TinyLlama":
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",

    "Phi-3 Mini":
        "microsoft/Phi-3-mini-4k-instruct",

    "Gemma":
        "google/gemma-2b-it"
}


class LLMLoader:

    def __init__(self):
        self.generator = None
        self.model_name = None

    def load_model(self, model_choice):

        model_id = SUPPORTED_MODELS.get(model_choice)

        if model_id is None:
            raise ValueError(
                f"Unsupported model: {model_choice}"
            )

        tokenizer = AutoTokenizer.from_pretrained(
            model_id
        )

        model = AutoModelForCausalLM.from_pretrained(
            model_id
        )

        self.generator = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=300,
            temperature=0.7,
            do_sample=True
        )

        self.model_name = model_choice

        return self.generator

    def get_generator(self):

        if self.generator is None:
            raise ValueError(
                "Model not loaded"
            )

        return self.generator


llm_loader = LLMLoader()
