import os
from prompts.chat_utils import chat, log
from prompts.prompt_utils import load_jinja2_template
from prompts.common_parser import parse_last_code_block as parser



def main(model, context_x, context_y, y, suggestion):
    template = load_jinja2_template(os.path.join(os.path.dirname(os.path.join(__file__)), "prompt.jinja2"))

    prompt = template.render(context_x=context_x,
                             context_y=context_y,
                             y=y,
                             suggestion=suggestion,)

    for response_msgs in chat([], prompt, model, parse_chat=True):
        newtext = parser(response_msgs)
        ret = {'text': newtext, 'response_msgs': response_msgs}
        yield ret
    
    log('根据意见重写正文', prompt, ret)
    
    return ret  


