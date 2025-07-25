
import re
validTags = ["b", "i", "em", "div", "p"]

def getCleanTag(strParam):
    return strParam.replace("<", "").replace(">", "").strip()

def getTags(strParam):
    tags = []
    tag = ""
    in_tag = False

    for char in strParam:
        if char == '<':
            in_tag = True
            tag = char
        elif char == '>':
            if in_tag:
                tag += char
                tags.append(getCleanTag(tag))
                tag = ""
                in_tag = False
        elif in_tag:
            tag += char

    return tags



validTags = ["b", "i", "em", "div", "p"]

# Precompile a regex for fast tag matching
TAG_PATTERN = re.compile(r"</?([a-zA-Z0-9]+)>")

def validateTags(strParam):
    if not strParam:
        return False

    matches = TAG_PATTERN.findall(strParam)

    for tag in matches:
        if tag not in validTags:
            return False

    # Also check for unmatched "<" or ">"
    if strParam.count("<") != strParam.count(">"):
        return False

    # Ensure every '<' starts a valid tag (either opening or closing)
    split = strParam.split("<")[1:]  # skip anything before the first <
    for s in split:
        if not any(s.startswith(tag + ">") or s.startswith("/" + tag + ">") for tag in validTags):
            return False

    return True


def CheckDOM(strParam):
    if not strParam.startswith('<') or not strParam.endswith('>'):
        return False

    if not validateTags(strParam):
        return False
    tags = getTags(strParam)

    if not tags or len(tags) % 2 != 0:
        return False

    if len(tags) > 2 and tags[0] != tags[-1][1:]:
        return False
    
    stack = []

    first_diff = ""
    for tag in tags:
        if tag.startswith('/'):
            if not stack or stack[-1] != tag[1:]:
                if tag[1:] not in validTags:
                    return False
                else :
                    if first_diff:
                        return False
                    first_diff = stack[-1]
            stack.pop()
        else:
            if tag in validTags:
                stack.append(tag)
            else:
                return False

    if not stack:
        if first_diff:
            return first_diff
        else:
            return True
    elif len(stack) == 1:
        return stack[0]
    else:
        return False  


print(CheckDOM(input()))


# exemples
# Input: "<div><p>hello</p></div>"
# 1. --> ["<div>", "<p>", "</p>", "</div>"]
# 2. -> Use stack
