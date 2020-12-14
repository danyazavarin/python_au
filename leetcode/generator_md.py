import sys

LEETCODE_END_LINK = '[comment]: <> (Stop)'


class LeetCodeSolution:
    def __init__(self, title, link, code):
        self.title = title.split('. ')[1].rstrip('\n')
        self.link = link.rstrip('\n')
        self.code = code

    def __str__(self):
        return 'title = {}, link = {}, code = {},'.format(self.title, self.link, self.code)

    def get_md_formatted_code(self):
        return '``` python\n{}\n```'.format('\n'.join(map(lambda x: x.strip('\n')[4:], self.code)))

    def get_md_title(self):
        return '# {}\n\n## {}\n'.format('Intervals', self.title)

    def get_md_solution_link(self):
        return '+ [{}](#{})'.format(self.title, self.link[30:-1])

    def get_md_formatted_solution(self):
        return ('{}\n{}\n\n{}\n\n{}'.format(self.get_md_title(), self.get_md_solution_link(), self.link,
                                            self.get_md_formatted_code()))


def read_all_lines_from(filename):
    file = open(filename)
    result = file.readlines()
    file.close()
    return result


def write_to_md(filename, data):
    file = open(filename, 'w')
    file.write(data)
    file.close()


def read_all_file(filename):
    file = open(filename)
    result = file.read()
    file.close()
    return result


def merge_solutions(old_solution, new_solution):
    old_splitted = old_solution.split(LEETCODE_END_LINK)
    if len(old_splitted) == 1:
        return '{}'.format(new_solution)
    return '{}{}{}'.format(old_splitted[0], new_solution, old_splitted[1])


def main():
    in_txt = read_all_lines_from('src.txt')
    source = LeetCodeSolution(in_txt[0], in_txt[1], in_txt[3:])
    new = source.get_md_formatted_solution()
    old = read_all_file('intervals.md')
    result = merge_solutions(old, new)
    write_to_md('intervals.md', result)


if __name__ == "__main__":
    main()