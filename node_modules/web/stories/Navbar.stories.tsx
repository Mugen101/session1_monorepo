import type { Meta, StoryObj } from '@storybook/react';
import { Navbar } from '../components/ui/Navbar';
import React from 'react';

const meta: Meta<typeof Navbar> = {
  title: 'Design System/Navbar',
  component: Navbar,
};
export default meta;

type Story = StoryObj<typeof Navbar>;

export const Default: Story = {};
