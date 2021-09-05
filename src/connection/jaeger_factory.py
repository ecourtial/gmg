import logging
from jaeger_client import Config

class JaegerTracer:

    @classmethod
    def init(cls, service):
        cls.mainSpan = None
        cls.spans = []

        logging.getLogger('').handlers = []
        logging.basicConfig(format='%(message)s', level=logging.DEBUG)

        config = Config(
            config={
                'sampler': {
                    'type': 'const',
                    'param': 1,
                },
                'local_agent': {
                    'reporting_host': '192.168.80.2',
                    'reporting_port': '6831',
                },
                'logging': True,
            },
            service_name=service,
        )

        # this call also sets opentracing.tracer
        cls.connection = config.initialize_tracer()

    @classmethod
    def createFirstSpan(cls):
        """Create the main span"""
        if cls.mainSpan is None:
            cls.mainSpan = cls.connection.start_span("Main span for the whole main request")
            cls.mainSpan.log_kv({'event': 'I am starting to log the main request', 'value': 'Go value yourself!'})
            cls.spans.append(cls.mainSpan)

    @classmethod
    def getChildSpan(cls, spanName, parent = None):
        """Get a new span"""
        if (parent is None):
            span = cls.connection.start_span(spanName, cls.mainSpan)
        else:
            span = cls.connection.start_span(spanName, child_of=parent)
        cls.spans.append(span)
        return span

    @classmethod
    def finishAllSpans(cls):
        for span in cls.spans:
            span.finish()
