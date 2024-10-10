class StepSubtracting:
    
    @staticmethod
    def run(orchestrator, pipeline) -> None:
        result=pipeline.result
        pipeline.result = orchestrator.bots.subtractor.sub(result)
        output = StepSubtracting.__format_output(pipeline,result)
        orchestrator.bots.printer.print_output(output)

    def __format_output(pipeline,result):
        return f"{pipeline.step} > {result} - 25% = {pipeline.result}"