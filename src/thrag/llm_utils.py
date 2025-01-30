import structlog
from litellm import completion

logger = structlog.get_logger(__name__)


def call_llm(prompt: str, model: str = "gpt-4", temperature: float = 0.0) -> str:
    """
    Wrapper around litellm to handle basic parameters and logging.
    """
    logger.debug("llm_call.start", model=model, prompt_length=len(prompt))
    response = completion(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        temperature=temperature,
    )
    assert isinstance(response, dict)
    content = response["choices"][0]["message"]["content"]
    usage = response["usage"]
    logger.debug(
        "llm_call.end",
        model=model,
        tokens_prompt=usage["prompt_tokens"],
        tokens_completion=usage["completion_tokens"],
        tokens_total=usage["total_tokens"],
    )
    return content
