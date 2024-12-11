import unittest

import unittest
from modelmetry.observability.span import CompletionSpan
from modelmetry.openapi.models import (
    Payload,
    CompletionFamilyData,
    CompletionPayload,
    Cost,
    Document,
    Money,
    Options,
    Usage,
    UsageValue,
)
from modelmetry.openapi.models.system_message import SystemMessage
from modelmetry.openapi.models.text_part import TextPart

# messages: List[
#     Union[SystemMessage, UserMessage, AssistantMessage, ToolMessage]
# ],


class TestCompletionSpan(unittest.TestCase):
    def setUp(self):
        self.trace_id = "trace_id"
        self.tenant_id = "tenant_id"
        self.parent_id = "parent_id"
        self.name = "name"
        self.message = "message"
        self.severity = "severity"
        self.family = "family"
        self.metadata = {"key": "value"}
        self.messages = []
        self.documents = [
            Document(
                Identifier="identifier",
                Title="title",
                ContentType="content_type",
                Content="content",
                Metadata={"key": "value"},
            )
        ]
        self.options = Options()
        self.usage = Usage(input=UsageValue(Amount=10, Unit="tokens"))
        self.cost = Cost(input=Money(Amount=10.0, Currency="USD"))

    def test_completion_span_creation(self):
        span = CompletionSpan(
            name=self.name,
            trace_id=self.trace_id,
            tenant_id=self.tenant_id,
            model="model",
            parent_id=self.parent_id,
            message=self.message,
            severity=self.severity,
            family=self.family,
            metadata=self.metadata,
            messages=self.messages,
            documents=self.documents,
            options=self.options,
            usage=self.usage,
            cost=self.cost,
        )

        self.assertEqual(span.name, self.name)
        self.assertEqual(span.trace_id, self.trace_id)
        self.assertEqual(span.tenant_id, self.tenant_id)
        self.assertEqual(span.parent_id, self.parent_id)
        self.assertEqual(span.message, self.message)
        self.assertEqual(span.severity, self.severity)
        self.assertEqual(span.family, self.family)
        self.assertEqual(span.metadata, self.metadata)
        self.assertEqual(span.family_data.options, self.options)
        self.assertEqual(span.family_data.documents, self.documents)
        self.assertEqual(span.family_data.messages, self.messages)
        self.assertEqual(span.family_data.usage, self.usage)
        self.assertEqual(span.family_data.cost, self.cost)

    def test_completion_span_set_model(self):
        span = CompletionSpan(
            name=self.name,
            trace_id=self.trace_id,
            tenant_id=self.tenant_id,
            model="model",
            parent_id=self.parent_id,
            message=self.message,
            severity=self.severity,
            family=self.family,
            metadata=self.metadata,
            documents=self.documents,
            options=self.options,
            usage=self.usage,
            cost=self.cost,
        )

        span.set_model("new_model")
        self.assertEqual(span.family_data.options.model, "new_model")

    def test_completion_span_set_provider(self):
        span = CompletionSpan(
            name=self.name,
            trace_id=self.trace_id,
            tenant_id=self.tenant_id,
            model="model",
            parent_id=self.parent_id,
            message=self.message,
            severity=self.severity,
            family=self.family,
            metadata=self.metadata,
            documents=self.documents,
            options=self.options,
            usage=self.usage,
            cost=self.cost,
        )

        span.set_provider("new_provider")
        self.assertEqual(span.family_data.options.provider, "new_provider")

    def test_completion_span_add_system_text(self):
        span = CompletionSpan(
            name=self.name,
            trace_id=self.trace_id,
            tenant_id=self.tenant_id,
            model="model",
            parent_id=self.parent_id,
            message=self.message,
            severity=self.severity,
            family=self.family,
            metadata=self.metadata,
            documents=self.documents,
            options=self.options,
            usage=self.usage,
            cost=self.cost,
        )

        span.add_system_text("the prompt")
        self.assertEqual(
            span.family_data.messages,
            [{"Role": "system", "Contents": [{"Text": "the prompt"}]}],
        )

    def test_completion_span_add_user_text(self):
        span = CompletionSpan(
            name=self.name,
            trace_id=self.trace_id,
            tenant_id=self.tenant_id,
            model="model",
            parent_id=self.parent_id,
            message=self.message,
            severity=self.severity,
            family=self.family,
            metadata=self.metadata,
            documents=self.documents,
            options=self.options,
            usage=self.usage,
            cost=self.cost,
        )

        span.add_user_text("the prompt")
        self.assertEqual(
            span.family_data.messages,
            [{"Role": "user", "Contents": [{"Text": "the prompt"}]}],
        )

    def test_completion_span_add_assistant_text(self):
        span = CompletionSpan(
            name=self.name,
            trace_id=self.trace_id,
            tenant_id=self.tenant_id,
            model="model",
            parent_id=self.parent_id,
            message=self.message,
            severity=self.severity,
            family=self.family,
            metadata=self.metadata,
            documents=self.documents,
            options=self.options,
            usage=self.usage,
            cost=self.cost,
        )

        span.add_assistant_text("the prompt")
        self.assertEqual(
            span.family_data.messages,
            [{"Role": "assistant", "Contents": [{"Text": "the prompt"}]}],
        )

    def test_completion_span_set_usage(self):
        span = CompletionSpan(
            name=self.name,
            trace_id=self.trace_id,
            tenant_id=self.tenant_id,
            model="model",
            parent_id=self.parent_id,
            message=self.message,
            severity=self.severity,
            family=self.family,
            metadata=self.metadata,
            documents=self.documents,
            options=self.options,
            usage=self.usage,
            cost=self.cost,
        )

        span.set_usage("input", 20, "tokens")
        self.assertEqual(
            span.family_data.usage.input, UsageValue(Amount=20, Unit="tokens")
        )

    def test_completion_span_set_cost(self):
        span = CompletionSpan(
            name=self.name,
            trace_id=self.trace_id,
            tenant_id=self.tenant_id,
            model="model",
            parent_id=self.parent_id,
            message=self.message,
            severity=self.severity,
            family=self.family,
            metadata=self.metadata,
            documents=self.documents,
            options=self.options,
            usage=self.usage,
            cost=self.cost,
        )

        span.set_cost("input", 20.0, "USD")
        self.assertEqual(
            span.family_data.cost.input, Money(Amount=20.0, Currency="USD")
        )

    def test_completion_span_add_document(self):
        span = CompletionSpan(
            name=self.name,
            trace_id=self.trace_id,
            tenant_id=self.tenant_id,
            model="model",
            parent_id=self.parent_id,
            message=self.message,
            severity=self.severity,
            family=self.family,
            metadata=self.metadata,
            documents=self.documents,
            options=self.options,
            usage=self.usage,
            cost=self.cost,
        )

        new_document = Document(
            Identifier="new_identifier",
            Title="new_title",
            ContentType="new_content_type",
            Content="new_content",
            Metadata={"new_key": "new_value"},
        )
        span.add_document(
            identifier=new_document.identifier,
            title=new_document.title,
            content_type=new_document.content_type,
            content=new_document.content,
            metadata=new_document.metadata,
        )
        self.assertEqual(span.family_data.documents, self.documents + [new_document])

    def test_completion_span_end(self):
        span = CompletionSpan(
            name=self.name,
            trace_id=self.trace_id,
            tenant_id=self.tenant_id,
            model="model",
            parent_id=self.parent_id,
            message=self.message,
            severity=self.severity,
            family=self.family,
            metadata=self.metadata,
            documents=self.documents,
            options=self.options,
            usage=self.usage,
            cost=self.cost,
        )

        span.end()
        self.assertIsNotNone(span.ended_at)
