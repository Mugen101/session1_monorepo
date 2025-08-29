import type { Meta, StoryObj } from '@storybook/react';
import { Card } from '../components/ui/Card';
import React from 'react';

const meta: Meta<typeof Card> = {
  title: 'Design System/Card',
  component: Card,
};
export default meta;

type Story = StoryObj<typeof Card>;

export const Default: Story = {
  args: {
    children: 'Card content',
  },
};
