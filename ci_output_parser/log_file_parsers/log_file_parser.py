import json

from ci_output_parser.formatter import format_lint_lines


class LogFileParser:

    def __init__(self, log_file_path=None, parser_name=None, output_file_name=None):
        """LogFileParser initializer

        Set log file path, parser name, and output file name.
        Use these to configure text and json file output file names.

        Args:
            log_file_path (string or None): path to log file to parse
            parser_name (string or None): name to use as the title for the parser output (default: Log File Lint)
            output_file_name (string or None): base name to use for the output files written (default: parser_name)
        """
        if log_file_path is None:
            raise ValueError("LogFileParser log_file_path must be a valid file path")
        self.log_file_path = log_file_path
        if parser_name is None:
            parser_name = "Log File Lint"
        self.parser_name = parser_name
        if output_file_name is None:
            output_file_name = parser_name.lower().replace(' ', '_')
            output_file_name = output_file_name.replace('-', '_')
        self.text_output_file_name = output_file_name + ".txt"
        self.json_output_file_name = output_file_name + ".json"
        self.log_lines = []
        self.lint_lines = []
        self.lint_errors = []
        self.formatted_lines = []
        # TODO: test
        self.lint_dictionary = {}

    def log_parser(self):
        """Parse log file and write text and json files with formatted lint lines.

        Runs these functions in this order:
            get_log_lines_from_file
            get_lint_lines
            get_lint_error_lines
            clean_lint_error_lines
            format_lint_errors
            write_lines_to_file
        """
        print("Running log parser for", self.parser_name)
        print("Getting log lines from log file", self.log_file_path)
        self.get_log_lines_from_file()
        print("Getting lint lines from %s log lines" % len(self.log_lines))
        self.get_lint_lines()
        print("Getting lint error lines from %s lint lines" % len(self.lint_lines))
        self.get_lint_error_lines()
        print("Cleaning lint error lines from %s lines" % len(self.lint_errors))
        self.clean_lint_error_lines()
        self.format_lint_errors()
        self.write_lines_to_file()
        print("Finished running log parser for", self.parser_name)

    def get_log_lines_from_file(self):
        """Get log lines from log file. Not implemented in LogFileParser.

        Handle self.log_file_path to set self.log_lines
        """
        raise NotImplementedError("Class %s doesn't implement get_log_lines_from_file()" % self.__class__.__name__)

    def get_lint_lines(self):
        """Get lint lines from log lines. Not implemented in LogFileParser.

        Handle self.log_lines to set self.lint_lines
        """
        raise NotImplementedError("Class %s doesn't implement get_lint_lines()" % self.__class__.__name__)

    def get_lint_error_lines(self):
        """Get lint error lines from lint lines. Not implemented in LogFileParser.

        Handle self.lint_lines to set self.lint_errors
        """
        raise NotImplementedError("Class %s doesn't implement get_lint_errors()" % self.__class__.__name__)

    def clean_lint_error_lines(self):
        """Get clean lint error lines from lint error lines. Not implemented in LogFileParser.

        Handle self.lint_errors to set self.lint_errors
        """
        raise NotImplementedError("Class %s doesn't implement clean_lint_error_lines()" % self.__class__.__name__)

    def format_lint_errors(self):
        """Get formatted lines from clean lint error lines if any.

        Handle self.lint_errors to set self.formatted_lines
        """
        if self.lint_errors:
            print("Formatting %s log lint lines" % len(self.lint_errors))
            self.formatted_lines = format_lint_lines(self.parser_name, self.lint_errors, self.formatted_lines)

    def write_lines_to_file(self):
        """Write formatted lines (if any) to files.

        Handle self.formatted_lines to write to files

        Returns:
            (boolean): Whether or not the files were written to successfully

        """
        write_success = False
        if self.formatted_lines:
            print("Writing %s log lint lines to text and json files" % len(self.lint_errors))
            write_success = self.write_formatted_lines_to_file()
        return write_success

    def write_formatted_lines_to_file(self):
        """Write formatted lines to text and json files.

        Handle self.formatted_lines to write to the self.text_output_file_name and self.json_output_file_name files

        Returns:
            (boolean): Whether or not the files were written to successfully

        """
        print("Writing to text file", self.text_output_file_name)
        text_file_write_success = self.output_lint_lines_to_file()
        self.make_json_dict_from_lint_lines()
        print("Writing to json file", self.json_output_file_name)
        json_file_write_success = self.output_lint_lines_to_json_file()
        return text_file_write_success and json_file_write_success

    # TODO: test
    def output_lint_lines_to_file(self):
        with open(self.text_output_file_name, 'w+') as file_object:
            file_object.writelines(self.formatted_lines)
            file_object.seek(0)
            number_of_lines = len(file_object.readlines())
        return number_of_lines == len(self.formatted_lines)

    # TODO: test
    def output_lint_lines_to_json_file(self):
        with open(self.json_output_file_name, 'w+') as outfile:
            json.dump(self.lint_dictionary, outfile)
            outfile.seek(0)
            payload = outfile.readline()
        return json.dumps(self.lint_dictionary.get("body")) in payload

    # TODO: test
    def make_json_dict_from_lint_lines(self):
        json_body_lines = ''.join(self.formatted_lines)
        self.lint_dictionary = {'body': json_body_lines}
